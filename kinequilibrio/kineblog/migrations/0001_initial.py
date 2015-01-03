# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AdvertPlacement'
        db.create_table(u'kineblog_advertplacement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='advert_placements', to=orm['wagtailcore.Page'])),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['kineblog.Advert'])),
        ))
        db.send_create_signal(u'kineblog', ['AdvertPlacement'])

        # Adding model 'Advert'
        db.create_table(u'kineblog_advert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='adverts', null=True, to=orm['wagtailcore.Page'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'kineblog', ['Advert'])

        # Adding model 'HomePageCarouselItem'
        db.create_table(u'kineblog_homepagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='carousel_items', to=orm['kineblog.HomePage'])),
        ))
        db.send_create_signal(u'kineblog', ['HomePageCarouselItem'])

        # Adding model 'HomePageRelatedLink'
        db.create_table(u'kineblog_homepagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.HomePage'])),
        ))
        db.send_create_signal(u'kineblog', ['HomePageRelatedLink'])

        # Adding model 'HomePage'
        db.create_table(u'kineblog_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('body', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'kineblog', ['HomePage'])

        # Adding model 'StandardIndexPageRelatedLink'
        db.create_table(u'kineblog_standardindexpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.StandardIndexPage'])),
        ))
        db.send_create_signal(u'kineblog', ['StandardIndexPageRelatedLink'])

        # Adding model 'StandardIndexPage'
        db.create_table(u'kineblog_standardindexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('feed_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['StandardIndexPage'])

        # Adding model 'StandardPageCarouselItem'
        db.create_table(u'kineblog_standardpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='carousel_items', to=orm['kineblog.StandardPage'])),
        ))
        db.send_create_signal(u'kineblog', ['StandardPageCarouselItem'])

        # Adding model 'StandardPageRelatedLink'
        db.create_table(u'kineblog_standardpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.StandardPage'])),
        ))
        db.send_create_signal(u'kineblog', ['StandardPageRelatedLink'])

        # Adding model 'StandardPage'
        db.create_table(u'kineblog_standardpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('body', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('feed_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['StandardPage'])

        # Adding model 'BlogIndexPageRelatedLink'
        db.create_table(u'kineblog_blogindexpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.BlogIndexPage'])),
        ))
        db.send_create_signal(u'kineblog', ['BlogIndexPageRelatedLink'])

        # Adding model 'BlogIndexPage'
        db.create_table(u'kineblog_blogindexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'kineblog', ['BlogIndexPage'])

        # Adding model 'BlogPageCarouselItem'
        db.create_table(u'kineblog_blogpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='carousel_items', to=orm['kineblog.BlogPage'])),
        ))
        db.send_create_signal(u'kineblog', ['BlogPageCarouselItem'])

        # Adding model 'BlogPageRelatedLink'
        db.create_table(u'kineblog_blogpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.BlogPage'])),
        ))
        db.send_create_signal(u'kineblog', ['BlogPageRelatedLink'])

        # Adding model 'BlogPageTag'
        db.create_table(u'kineblog_blogpagetag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'kineblog_blogpagetag_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('modelcluster.fields.ParentalKey')(related_name='tagged_items', to=orm['kineblog.BlogPage'])),
        ))
        db.send_create_signal(u'kineblog', ['BlogPageTag'])

        # Adding model 'BlogPage'
        db.create_table(u'kineblog_blogpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('body', self.gf('wagtail.wagtailcore.fields.RichTextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('feed_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['BlogPage'])

        # Adding model 'PersonPageRelatedLink'
        db.create_table(u'kineblog_personpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.PersonPage'])),
        ))
        db.send_create_signal(u'kineblog', ['PersonPageRelatedLink'])

        # Adding model 'PersonPage'
        db.create_table(u'kineblog_personpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('direccion_1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('direccion_2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('biography', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
            ('feed_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['PersonPage'])

        # Adding model 'ContactPage'
        db.create_table(u'kineblog_contactpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('direccion_1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('direccion_2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('body', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('feed_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['ContactPage'])

        # Adding model 'EventIndexPageRelatedLink'
        db.create_table(u'kineblog_eventindexpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.EventIndexPage'])),
        ))
        db.send_create_signal(u'kineblog', ['EventIndexPageRelatedLink'])

        # Adding model 'EventIndexPage'
        db.create_table(u'kineblog_eventindexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'kineblog', ['EventIndexPage'])

        # Adding model 'EventPageCarouselItem'
        db.create_table(u'kineblog_eventpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='carousel_items', to=orm['kineblog.EventPage'])),
        ))
        db.send_create_signal(u'kineblog', ['EventPageCarouselItem'])

        # Adding model 'EventPageRelatedLink'
        db.create_table(u'kineblog_eventpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='related_links', to=orm['kineblog.EventPage'])),
        ))
        db.send_create_signal(u'kineblog', ['EventPageRelatedLink'])

        # Adding model 'EventPageSpeaker'
        db.create_table(u'kineblog_eventpagespeaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtailcore.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='speakers', to=orm['kineblog.EventPage'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['EventPageSpeaker'])

        # Adding model 'EventPage'
        db.create_table(u'kineblog_eventpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('date_from', self.gf('django.db.models.fields.DateField')()),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('time_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('audience', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('signup_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('feed_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['wagtailimages.Image'])),
        ))
        db.send_create_signal(u'kineblog', ['EventPage'])

        # Adding model 'FormField'
        db.create_table(u'kineblog_formfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('choices', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='form_fields', to=orm['kineblog.FormPage'])),
        ))
        db.send_create_signal(u'kineblog', ['FormField'])

        # Adding model 'FormPage'
        db.create_table(u'kineblog_formpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('to_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('from_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('thank_you_text', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'kineblog', ['FormPage'])


    def backwards(self, orm):
        # Deleting model 'AdvertPlacement'
        db.delete_table(u'kineblog_advertplacement')

        # Deleting model 'Advert'
        db.delete_table(u'kineblog_advert')

        # Deleting model 'HomePageCarouselItem'
        db.delete_table(u'kineblog_homepagecarouselitem')

        # Deleting model 'HomePageRelatedLink'
        db.delete_table(u'kineblog_homepagerelatedlink')

        # Deleting model 'HomePage'
        db.delete_table(u'kineblog_homepage')

        # Deleting model 'StandardIndexPageRelatedLink'
        db.delete_table(u'kineblog_standardindexpagerelatedlink')

        # Deleting model 'StandardIndexPage'
        db.delete_table(u'kineblog_standardindexpage')

        # Deleting model 'StandardPageCarouselItem'
        db.delete_table(u'kineblog_standardpagecarouselitem')

        # Deleting model 'StandardPageRelatedLink'
        db.delete_table(u'kineblog_standardpagerelatedlink')

        # Deleting model 'StandardPage'
        db.delete_table(u'kineblog_standardpage')

        # Deleting model 'BlogIndexPageRelatedLink'
        db.delete_table(u'kineblog_blogindexpagerelatedlink')

        # Deleting model 'BlogIndexPage'
        db.delete_table(u'kineblog_blogindexpage')

        # Deleting model 'BlogPageCarouselItem'
        db.delete_table(u'kineblog_blogpagecarouselitem')

        # Deleting model 'BlogPageRelatedLink'
        db.delete_table(u'kineblog_blogpagerelatedlink')

        # Deleting model 'BlogPageTag'
        db.delete_table(u'kineblog_blogpagetag')

        # Deleting model 'BlogPage'
        db.delete_table(u'kineblog_blogpage')

        # Deleting model 'PersonPageRelatedLink'
        db.delete_table(u'kineblog_personpagerelatedlink')

        # Deleting model 'PersonPage'
        db.delete_table(u'kineblog_personpage')

        # Deleting model 'ContactPage'
        db.delete_table(u'kineblog_contactpage')

        # Deleting model 'EventIndexPageRelatedLink'
        db.delete_table(u'kineblog_eventindexpagerelatedlink')

        # Deleting model 'EventIndexPage'
        db.delete_table(u'kineblog_eventindexpage')

        # Deleting model 'EventPageCarouselItem'
        db.delete_table(u'kineblog_eventpagecarouselitem')

        # Deleting model 'EventPageRelatedLink'
        db.delete_table(u'kineblog_eventpagerelatedlink')

        # Deleting model 'EventPageSpeaker'
        db.delete_table(u'kineblog_eventpagespeaker')

        # Deleting model 'EventPage'
        db.delete_table(u'kineblog_eventpage')

        # Deleting model 'FormField'
        db.delete_table(u'kineblog_formfield')

        # Deleting model 'FormPage'
        db.delete_table(u'kineblog_formpage')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'kineblog.advert': {
            'Meta': {'object_name': 'Advert'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'adverts'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'kineblog.advertplacement': {
            'Meta': {'object_name': 'AdvertPlacement'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['kineblog.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'advert_placements'", 'to': u"orm['wagtailcore.Page']"})
        },
        u'kineblog.blogindexpage': {
            'Meta': {'object_name': 'BlogIndexPage', '_ormbases': [u'wagtailcore.Page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'kineblog.blogindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.BlogIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.blogpage': {
            'Meta': {'object_name': 'BlogPage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'kineblog.blogpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['kineblog.BlogPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.blogpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.BlogPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.blogpagetag': {
            'Meta': {'object_name': 'BlogPageTag'},
            'content_object': ('modelcluster.fields.ParentalKey', [], {'related_name': "'tagged_items'", 'to': u"orm['kineblog.BlogPage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'kineblog_blogpagetag_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'kineblog.contactpage': {
            'Meta': {'object_name': 'ContactPage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'direccion_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'direccion_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'kineblog.eventindexpage': {
            'Meta': {'object_name': 'EventIndexPage', '_ormbases': [u'wagtailcore.Page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'kineblog.eventindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.EventIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.eventpage': {
            'Meta': {'object_name': 'EventPage', '_ormbases': [u'wagtailcore.Page']},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'signup_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'time_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.eventpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['kineblog.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.eventpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.eventpagespeaker': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageSpeaker'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'speakers'", 'to': u"orm['kineblog.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.formfield': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'FormField'},
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'form_fields'", 'to': u"orm['kineblog.FormPage']"}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.formpage': {
            'Meta': {'object_name': 'FormPage'},
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'thank_you_text': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'kineblog.homepage': {
            'Meta': {'object_name': 'HomePage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'kineblog.homepagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['kineblog.HomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.homepagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.HomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.personpage': {
            'Meta': {'object_name': 'PersonPage', '_ormbases': [u'wagtailcore.Page']},
            'biography': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'direccion_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'direccion_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'kineblog.personpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'PersonPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.PersonPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.standardindexpage': {
            'Meta': {'object_name': 'StandardIndexPage', '_ormbases': [u'wagtailcore.Page']},
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'kineblog.standardindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.StandardIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'kineblog.standardpage': {
            'Meta': {'object_name': 'StandardPage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'kineblog.standardpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['kineblog.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'kineblog.standardpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['kineblog.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'wagtailcore.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'expired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'go_live_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'has_unpublished_changes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_revision_created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_pages'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'search_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'wagtaildocs.document': {
            'Meta': {'object_name': 'Document'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'wagtailimages.image': {
            'Meta': {'object_name': 'Image'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'focal_point_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'focal_point_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'focal_point_x': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'focal_point_y': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['kineblog']