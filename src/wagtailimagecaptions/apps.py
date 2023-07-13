from django.apps import AppConfig


class WagtailImageCaptionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wagtailimagecaptions"

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals  # noqa
