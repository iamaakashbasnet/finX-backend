# Generated by Django 5.1.1 on 2024-10-19 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("portfolios", "0002_clientportfolio_firm_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PortfolioEntry",
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
                ("object_id", models.PositiveIntegerField()),
                ("date", models.DateField()),
                ("company_name", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("rate", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Portfolio Entry",
                "verbose_name_plural": "Portfolio Entries",
            },
        ),
    ]
