# Generated by Django 4.0.6 on 2022-10-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alpine", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Complain",
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
                ("text", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]