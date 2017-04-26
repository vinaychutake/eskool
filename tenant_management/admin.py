from django.contrib import admin

from tenant_management import models

# Register your models here.
admin.site.register(models.Institute)
admin.site.register(models.ContactNumber)
admin.site.register(models.Address)
admin.site.register(models.State)
admin.site.register(models.City)