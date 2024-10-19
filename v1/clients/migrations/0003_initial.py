# Generated by Django 5.1.1 on 2024-10-19 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clients", "0002_initial"),
        ("firms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="generalclient",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="poolinvestmentclient",
            name="firm",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="firms.firm"
            ),
        ),
        migrations.AddField(
            model_name="poolinvestmentclient",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]