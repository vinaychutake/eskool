from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from academics_management.views import views as academic_views

urlpatterns = [

    url(r'academics_management/$',
    	login_required(academic_views.AcademicsManagement.as_view()),
    	name='academics_management'),

    url(r'standard_template/$',
    	login_required(academic_views.StandardTemplate.as_view()),
    	name='standard_template'),

    url(r'manage_std_templates/$',
    	login_required(academic_views.ManageSTDTemplate.as_view()),
    	name='manage_std_templates'),

    url(r'update/(?P<std_template_id>\d+)/$',
    	login_required(academic_views.UpdateSTDTemplate.as_view()),
    	name='update_std_template'),

    url(r'create/$',
        login_required(academic_views.CreateSTDTemplate.as_view()),
        name='create_std_template'),

    url(r'delete/(?P<std_template_id>\d+)/$',
        login_required(academic_views.DeleteSTDTemplate.as_view()),
        name='delete_std_template'),

]