from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page

IMAGE_MODEL_CLASS = get_image_model_string()


class BlogPage(Page):
    body = RichTextField()
    created_on = models.DateTimeField(verbose_name="Created On", auto_now_add=True)
    thumbnail = models.ForeignKey(
        IMAGE_MODEL_CLASS, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    parent_page_types = ["wagtailcore.Page"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("thumbnail"),
    ]
