from django.apps import AppConfig


class WagtailImageCaptionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wagtailimagecaptions"

    def ready(self):
        # Register CaptionedImage for referencing (usage stats).
        from wagtail.models.reference_index import ReferenceIndex

        from .models import CaptionedImage

        ReferenceIndex.register_model(CaptionedImage)

        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals  # noqa
