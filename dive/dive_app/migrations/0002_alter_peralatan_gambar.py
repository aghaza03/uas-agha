# Generated by Django 4.1.1 on 2023-01-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="peralatan",
            name="gambar",
            field=models.ImageField(blank=True, null=True, upload_to="image/"),
        ),
    ]
