from django.contrib import admin
from academics_management.models import Subject, AcademicYear, StandardTemplate, Standard

admin.site.register([Subject, AcademicYear, StandardTemplate, Standard])
