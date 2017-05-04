from django.contrib import admin

from academics_management.models import Subject, AcademicYear

admin.site.register([Subject, AcademicYear])
