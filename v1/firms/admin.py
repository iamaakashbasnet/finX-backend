from django.contrib import admin

from .models import Firm, Domain

# Admin site customization
admin.site.site_header = "finX Admin"
admin.site.site_title = "finX Admin Portal"
admin.site.index_title = "Welcome to the finX Admin Dashboard"


class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(Firm)
        self.register(Domain)


tenant_admin_site = TenantAdminSite(name='tenant_admin_site')
