from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from academics_management.views import views as academic_views
from academics_management.views import subject_views as subject_views
from academics_management.views import year_views
from academics_management.views import template_views

urlpatterns = [

    url(r'academics_management/$',
       login_required(academic_views.AcademicsManagement.as_view()),
        name='academics_management'),

    url(r'standard_template/$',
    	login_required(template_views.StandardTemplate.as_view()),
    	name='standard_template'),

    url(r'manage_std_templates/$',
    	login_required(template_views.ManageSTDTemplate.as_view()),
    	name='manage_std_templates'),

    url(r'update_template/(?P<std_template_id>\d+)/$',
    	login_required(template_views.UpdateSTDTemplate.as_view()),
    	name='update_std_template'),

    url(r'create_template/$',
        login_required(template_views.CreateSTDTemplate.as_view()),
        name='create_std_template'),

    url(r'delete_template/(?P<std_template_id>\d+)/$',
        login_required(template_views.DeleteSTDTemplate.as_view()),
        name='delete_std_template'),

    url(r'subject_management/$',
        login_required(subject_views.SubjectManagement.as_view()),
        name='subject_management'),

   url(r'subjects/$',
        login_required(subject_views.GetSubjects.as_view()),
        name='subjects'),

    url(r'update/(?P<subject_id>\d+)/$',
        login_required(subject_views.UpdateSubject.as_view()),
        name='update_subject'),

    url(r'delete/(?P<subject_id>\d+)/$',
        login_required(subject_views.DeleteSubject.as_view()),
        name='delete_subject'),

    url(r'create/$',
        login_required(subject_views.CreateSubject.as_view()),
        name='create_subject'),

    url(r'academic_year/$',
        login_required(year_views.AcademicsYearView.as_view()),
        name='academic_year'),

    url(r'create_acadamy_year/$',
        login_required(year_views.CreateAcademicsYear.as_view()),
        name='create_acadamy_year'),

    url(r'all_academic_years/$',
        login_required(year_views.AcademicYear.as_view()),
        name='all_academic_years'),

    url(r'update_year/(?P<year_id>\d+)/$',
        login_required(year_views.UpdateYear.as_view()),
        name='update_year'),

    url(r'delete_year/(?P<year_id>\d+)/$',
        login_required(year_views.DeleteYear.as_view()),
        name='delete_year'),
]