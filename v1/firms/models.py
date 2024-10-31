from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Firm(TenantMixin):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


class Domain(DomainMixin):
    pass
