from django.db import models

from wagtail.fields import RichTextField
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.search import index


class CaptionedImage(AbstractImage):
    alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Set the image alt text used for accessibility.",
    )
    caption = RichTextField(features=["bold", "italic"], null=True, blank=True, help_text="Set the image caption.")
    credit = models.CharField(max_length=255, blank=True, help_text="Set the image credit.")
    iptc_data = models.JSONField(null=True, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        "credit",
        "alt",
        "caption",
    )

    search_fields = AbstractImage.search_fields + [
        index.SearchField("caption", partial_match=True, boost=10),
    ]

    def default_alt_text(self):
        """ Return our stored alt value, otherwise Wagtail defaults to the title. """
        if self.alt:
            return self.alt
        return super().default_alt_text


class CaptionedRendition(AbstractRendition):
    image = models.ForeignKey(CaptionedImage, on_delete=models.CASCADE, related_name="renditions")

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
