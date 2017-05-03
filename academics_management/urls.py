from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from academics_management.views import views as academic_views

urlpatterns = [

    url(r'academics_management/$',
    	login_required(academic_views.AcademicsManagement.as_view()),
    	name='academics_management'),
]