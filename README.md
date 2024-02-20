# Captions for Wagtail Images

A Django app for extending the Wagtail Image model to add captions and alt fields as
well as the extraction of IPTC image meta data.

![screenshot](https://github.com/newshour/wagtailimagecaptions/assets/14984514/278f5d01-7f2e-48a8-98fd-aaaa6c2d6b8c)

## Installing

Install using pip:

```sh
pip install wagtailimagecaptions
```

### Settings

In your settings file, add `wagtailimagecaptions` to `INSTALLED_APPS`:

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

### Migrating

Heads up! If you have existing images, you will need to create a [data migration operation](https://docs.wagtail.org/en/latest/advanced_topics/images/custom_image_model.html#migrating-from-the-builtin-image-model) to move the old images into
the new model.

## How to Use

The custom Image model, `CaptionedImage`, adds four new fields to the Wagtail Image model: `alt`, `caption`, `credit`, `iptc_data`. When a new image is uploaded via Wagtail's media library, the app will attempt to extract any IPTC meta data found in the file and fill
the `alt`, `caption` and `credit` fields. All IPTC meta data  extracted is also stored in `iptc_data`.

Example use in a template:

```python
{% load wagtailcore_tags %}

<img src="{{ image.url }}" alt="{{ image.alt }}">{{ image.caption|richtext }}
```

#### Adding date paths to image uploads.

To add date paths to the image upload path, you can set `WAGTIALIMAGECAPTIONS_UPLOAD_TO_DATE_PATH` in your Django settings file with a valid date format.

```python
# settings.py
WAGTIALIMAGECAPTIONS_UPLOAD_TO_DATE_PATH = "%Y/%m"
```