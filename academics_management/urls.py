from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from academics_management.views import views as academic_views
from academics_management.views import subject_views as subject_views
from academics_management.views import year_views

urlpatterns = [

    url(r'academics_management/$',
        login_required(academic_views.AcademicsManagement.as_view()),
        name='academics_management'),

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