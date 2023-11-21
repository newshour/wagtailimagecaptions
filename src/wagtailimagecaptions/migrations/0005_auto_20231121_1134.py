# Generated by Django 4.2 on 2023-11-21 11:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimagecaptions", "0004_auto_20231121_1134"),
    ]

    operations = [
        migrations.AlterField(
            model_name="captionedimage",
            name="uuid",
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
