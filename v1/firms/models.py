from django.contrib.auth import get_user_model
from django.db import models


class Firm(models.Model):
    name = models.CharField(max_length=255)
    managers = models.ManyToManyField(get_user_model(), related_name='managed_firms', blank=True)

    def __str__(self):
        return self.name
