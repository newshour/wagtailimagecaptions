import uuid

from django.db import models
from wagtail.fields import RichTextField
from wagtail.images.models import AbstractImage, AbstractRendition, Image
from wagtail.search import index


class CaptionedImage(AbstractImage):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Set the image alt text used for accessibility.",
    )
    caption = RichTextField(features=["bold", "italic"], null=True, blank=True, help_text="Set the image caption.")
    credit = models.CharField(
        max_length=255,
        blank=True,
        help_text="The name of the provider (e.g. AP, Getty, Reuters).",
    )
    byline = models.CharField(
        max_length=255,
        blank=True,
        help_text="The name(s) of the creator(s) of the image.",
    )
    usage_terms = models.CharField(
        max_length=255,
        blank=True,
        help_text="Rights information and usage limitations associated with the image, including any special restrictions or instructions.",
    )
    copyright_notice = models.CharField(
        max_length=255,
        blank=True,
        help_text="Any necessary copyright notice(s).",
    )
    iptc_data = models.JSONField(null=True, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        "credit",
        "byline",
        "alt",
        "caption",
        "usage_terms",
        "copyright_notice",
    )

    search_fields = AbstractImage.search_fields + [
        index.SearchField("uuid"),
        index.SearchField("caption"),
    ]

    def default_alt_text(self):
        """Return our stored alt value, otherwise Wagtail defaults to the title."""
        if self.alt:
            return self.alt
        return super().default_alt_text


class CaptionedRendition(AbstractRendition):
    image = models.ForeignKey(CaptionedImage, on_delete=models.CASCADE, related_name="renditions")

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
