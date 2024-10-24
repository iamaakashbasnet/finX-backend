# Generated by Django 5.1.1 on 2024-10-19 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("firms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="firm",
            name="managers",
            field=models.ManyToManyField(
                blank=True, related_name="managed_firms", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
