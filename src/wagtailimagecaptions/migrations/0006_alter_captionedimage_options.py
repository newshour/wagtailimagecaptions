# Generated by Django 4.2.12 on 2024-05-31 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimagecaptions", "0005_auto_20231121_1134"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="captionedimage",
            options={
                "permissions": [("choose_image", "Can choose image")],
                "verbose_name": "image",
                "verbose_name_plural": "images",
            },
        ),
    ]
