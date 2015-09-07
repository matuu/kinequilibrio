# encoding=utf-8
__author__ = 'm4tuu'
import os
import re
import time

from fabric.api import env, local, cd, abort, sudo, get, put, task, runs_once, run
from fabric.colors import green, red
from fabric.contrib.console import confirm
from fabric.contrib.project import rsync_project

env.hosts = ["www.kinequilibrio.com.ar"]
env.user = 'matuu'
env.key_filename = '/home/m4tuu/.ssh/id_rsa'


# remote paths
code_dir = "/home/matuu/kinequilibrio/kinequilibrio"
proj_dir = code_dir  # os.path.join(code_dir, ".")
remote_media = os.path.join(proj_dir, "media")

# local
virtualenv_dir = "/home/matuu/.virtualenvs/kinequilibrio"
virtualenv_name = "kinequilibrio"
local_media = os.path.join(os.path.abspath(os.path.dirname(__file__)), "media")

# directorio local para backups
backup_dir = "bkp-dbs"

def run_cmd_env(command):
    """
    Ejecuta un comando con el ve activado
    """
    # Con virtualenv
    run("source %(ve_dir)s/bin/activate; %(cmd)s" % {
       've_dir': virtualenv_dir,
       'cmd': command,
    })


@task
def run_backup():
    """
    Realiza un backup de la base de datos y la almacena localmente.
    """
    host = re.search("([\w.-]+)[:]?", env.host).group()
    date = time.strftime('%Y%m%d%H%M%S')
    fname = '%(host)s-backup-%(date)s.gz' % {'date': date, 'host': host}
    green("Ingrese la contraseña de la clave privada local.")
    sudo("pg_dump kine | gzip > /tmp/%s" % fname, user="postgres")
    get("/tmp/%s" % fname, os.path.join(backup_dir, fname))
    sudo("rm /tmp/%s" % fname, user="postgres")


@task
def deploy(backup=True):
    """
    Deploy to the selected servers, arguments: test, backup
    """
    if not confirm(green("¿Seguro que querés deployear?")):
        abort(red("Abortado por el usuario."))

    current_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
    if current_branch != 'master':
        abort(red("Abortado, no estás en el branch master."))

    if backup:
        green("Realizando backup de la base de datos y descargando copia.")
        run_backup()

    with cd(code_dir):
        green("Actualizando codigo")
        run("git pull")
        green("Actualizando dependencias")
        run_cmd_env("pip --exists-action b install -r ../requirements.txt")
    with cd(proj_dir):
        run_cmd_env("python manage.py migrate")
        sudo("service uwsgi restart")
        sudo("service nginx restart")
        run_cmd_env("python manage.py collectstatic --noinput")


def prepare_deployment(branch_name):
    local('python manage.py test --settings=kinequilibrio.settings_test')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)
    green("OK")


@task
def update_remote_db():
    """
    Reemplza la db remota con un backup de la local.

    Realiza un backup antes de la operación
    """
    run_backup()
    local("sudo -u postgres -H pg_dump kine > /tmp/dbk.bak")
    put(local_path="/tmp/dbk.bak", remote_path="/tmp/dbk.bak")
    sudo("dropdb kine", user="postgres")
    sudo("createdb kine", user="postgres")
    sudo("psql kine < /tmp/dbk.bak", user="postgres")
    sudo("psql kine -c \"GRANT ALL ON ALL TABLES IN SCHEMA public to kine;\"", user="postgres")
    sudo("psql kine -c \"GRANT ALL ON ALL SEQUENCES IN SCHEMA public to kine;\"", user="postgres")
    sudo("psql kine -c \"GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to kine;\"", user="postgres")
    sudo("rm /tmp/dbk.bak")
    local("sudo rm /tmp/dbk.bak")


@task
def rsync_media(dlt="yes"):
    """
    Sube los archivos media al servidor
    """
    rsync_project(remote_media, local_media + "/",
                  delete=True if dlt == "yes" else False)
