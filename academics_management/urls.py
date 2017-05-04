from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from academics_management.views import views as academic_views
from academics_management.views import subject_views as subject_views
from academics_management.views import year_views
from academics_management.views import template_views

urlpatterns = [

    #Standard Template Urls
    url(r'standard_template_management/$',
    	login_required(template_views.StandardTemplateManagement.as_view()),
    	name='standard_template_management'),

    url(r'std_templates/$',
    	login_required(template_views.STDTemplates.as_view()),
    	name='std_templates'),

    url(r'standard_template/create/$',
        login_required(template_views.CreateSTDTemplate.as_view()),
        name='create_std_template'),

    url(r'standard_template/update/(?P<std_template_id>\d+)/$',
    	login_required(template_views.UpdateSTDTemplate.as_view()),
    	name='update_std_template'),

    url(r'standard_template/delete/(?P<std_template_id>\d+)/$',
        login_required(template_views.DeleteSTDTemplate.as_view()),
        name='delete_std_template'),

    #Subject urls
    url(r'subject_management/$',
        login_required(subject_views.SubjectManagement.as_view()),
        name='subject_management'),

    url(r'subjects/$',
        login_required(subject_views.GetSubjects.as_view()),
        name='subjects'),

    url(r'subject/create/$',
        login_required(subject_views.CreateSubject.as_view()),
        name='create_subject'),

    url(r'subject/update/(?P<subject_id>\d+)/$',
        login_required(subject_views.UpdateSubject.as_view()),
        name='update_subject'),

    url(r'subject/delete/(?P<subject_id>\d+)/$',
        login_required(subject_views.DeleteSubject.as_view()),
        name='delete_subject'),


    #Academic year urls
    url(r'academic_year_management/$',
        login_required(year_views.AcademicYearManagement.as_view()),
        name='academic_year_management'),

    url(r'academic_years/$',
        login_required(year_views.GetAcademicYears.as_view()),
        name='academic_years'),

    url(r'academic_year/create/$',
        login_required(year_views.CreateAcademicYear.as_view()),
        name='create_academic_year'),

    url(r'academic_year/update/(?P<year_id>\d+)/$',
        login_required(year_views.UpdateYear.as_view()),
        name='update_academic_year'),

    url(r'academic_year/delete/(?P<year_id>\d+)/$',
        login_required(year_views.DeleteYear.as_view()),
        name='delete_academic_year'),
]