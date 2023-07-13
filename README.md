# Captions for Wagtail Images

A Django app for extending the Wagtail Image model to add captions and alt fields as
well as the extraction of IPTC image meta data.

### Settings

In your settings file, add `wagtailmedia` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "wagtailimagecaptions",
    # ...
]
```

You will also need to set a custom Image model in your setting files:

```python
# settings.py
WAGTAILIMAGES_IMAGE_MODEL = "wagtailimagecaptions.CaptionedImage"
```