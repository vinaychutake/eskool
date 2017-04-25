from django.contrib import admin

from staff_management.models import Staff, StaffType, Teacher

admin.site.register(StaffType)
admin.site.register(Staff)
admin.site.register(Teacher)
