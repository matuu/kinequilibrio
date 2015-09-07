# encoding=utf8
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


# Related links
class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class BlogIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('BlogIndexPage', related_name='related_links')


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    @property
    def blogs(self):
        # Get list of live blog pages that are descendants of this page
        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request):
        # Get blogs
        blogs = self.blogs

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs, 10)  # Show 10 blogs per page
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        tags = BlogPageTag.objects.annotate(
            count=models.Count('tag__kine_blog_blogpagetag_items', distinct=True)).values(
                'count', 'tag__name').distinct().order_by('-count', 'tag__name')[:10]

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        context['tags'] = tags
        return context

    content_panels = Page.content_panels + [
            FieldPanel('title', classname="full title"),
            FieldPanel('intro', classname="full"),
            InlinePanel('related_links', label="Related links"),
    ]


# Blog page

#class BlogPageCarouselItem(Orderable, CarouselItem):
    #page = ParentalKey('kine_blog.BlogPage', related_name='carousel_items')


class BlogPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('kine_blog.BlogPage', related_name='related_links')


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('kine_blog.BlogPage', related_name='tagged_items')


class BlogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField("Post date")
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    @property
    def get_tags(self):
        return self.tags.all()

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

    def get_context(self, request):

        tags = BlogPageTag.objects.annotate(
            count=models.Count('tag__kine_blog_blogpagetag_items', distinct=True)).values(
                'count', 'tag__name').distinct().order_by('-count', 'tag__name')[:10]

        # Update template context
        context = super(BlogPage, self).get_context(request)
        context['tags'] = tags

        return context

BlogPage.content_panels = Page.content_panels + [
    FieldPanel('date'),
    ImageChooserPanel('main_image'),
    FieldPanel('intro'),
    FieldPanel('body'),
    InlinePanel(BlogPage, 'related_links', label="Related links"),
]

BlogPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    # ImageChooserPanel('main_image'),
    FieldPanel('tags'),
]
