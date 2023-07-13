# Captions for Wagtail Images

A Django app for extending the Wagtail Image model to add captions and alt fields as
well as the extraction of IPTC image meta data.

![screenshot](https://github.com/newshour/wagtailimagecaptions/assets/14984514/278f5d01-7f2e-48a8-98fd-aaaa6c2d6b8c)

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
