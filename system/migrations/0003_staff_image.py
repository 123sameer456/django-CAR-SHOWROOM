# Generated by Django 4.2.2 on 2023-07-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("system", "0002_rename_brand_model_engine_engine_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]