from django.contrib import admin
from .models import Tenant, Domain


# Register your models here.
class TenantAdminSite(admin.AdminSite):
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(Tenant)
        self.register(Domain)

tenant_admin_site = TenantAdminSite(name="tenant_Admin_site")