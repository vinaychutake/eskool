from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from academics_management.views import views as academic_views
from academics_management.views import subject_views as subject_views

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
    	name='delete_notice'),		 	 
]