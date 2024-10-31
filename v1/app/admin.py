from django.contrib import admin

from v1.app.models import Firm, Domain


class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(Firm)
        self.register(Domain)


tenant_admin_site = TenantAdminSite(name='tenant_admin_site')
