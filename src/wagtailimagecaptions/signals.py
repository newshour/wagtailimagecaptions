from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import Truncator
from wagtail.images import get_image_model_string

from .services import parse_iptc

IMAGE_MODEL = get_image_model_string()


@receiver(pre_save, sender=IMAGE_MODEL)
def parse_image_meta(sender, **kwargs):
    """
    Parses image meta data from a tif or jpeg and populates the corresponding
    fields of the image model.
    """
    instance = kwargs["instance"]

    # If we have an ID, don't parse again.
    if instance.id is not None:
        return

    meta_dict = parse_iptc(instance.file)

    # Add the meta data to the fields.
    if title := Truncator(meta_dict.get("headline", "")).chars(255):
        instance.title = title
        instance.alt = title

    instance.credit = Truncator(meta_dict.get("credit", "")).chars(255)
    instance.caption = meta_dict.get("caption")
    instance.iptc_data = meta_dict
