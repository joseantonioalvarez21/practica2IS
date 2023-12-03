# Generated by Django 4.2.5 on 2023-09-27 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("relecloud", "0003_cruise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cruise",
            name="destinations",
            field=models.ManyToManyField(
                related_name="cruises", to="relecloud.destination"
            ),
        ),
        migrations.CreateModel(
            name="InfoRequest",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("notes", models.TextField(max_length=2000)),
                (
                    "cruise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="relecloud.cruise",
                    ),
                ),
            ],
        ),
    ]
