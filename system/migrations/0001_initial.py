# Generated by Django 4.2.2 on 2023-07-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand_name",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "feature_name",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ShowRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="unamed", max_length=200, null=True)),
                (
                    "location",
                    models.CharField(default="not defined", max_length=200, null=True),
                ),
                (
                    "contact",
                    models.CharField(default="not defined", max_length=200, null=True),
                ),
                ("email", models.EmailField(max_length=200, unique=True)),
                ("capacity", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                (
                    "last_name",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                (
                    "designation",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                (
                    "contact",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                ("email", models.EmailField(max_length=200, unique=True)),
                ("join_date", models.DateField()),
                (
                    "showroom_staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="system.showroom",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Modell",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model_name",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                (
                    "brand",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                ("year", models.IntegerField(null=True)),
                ("price", models.DecimalField(decimal_places=10, max_digits=19)),
                (
                    "brand_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="system.brand"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Engine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "engine_type",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                ("horse_power", models.IntegerField(null=True)),
                (
                    "fuel_type",
                    models.CharField(default="unamed", max_length=200, null=True),
                ),
                (
                    "brand_model",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="system.modell"
                    ),
                ),
            ],
        ),
    ]
