from django.conf.urls import url
from django.contrib import admin

from staff_management import views as sm_views

urlpatterns = [

    url(r'teacher/create/$', sm_views.CreateTeacher.as_view(),
        name='create_teacher'),

    url(r'teacher/(?P<teacher_id>\d+)/$',
        sm_views.UpdateTeacher.as_view(),
        name='update_teacher'),

    url(r'teacher/delete/(?P<teacher_id>\d+)/$',
        sm_views.DeleteTeacher.as_view(),
        name='delete_teacher'),

    url(r'teacher/upload/$',
        sm_views.UploadTeachers.as_view(),
        name='upload_teachers'),

    url(r'teacher/profile/(?P<teacher_id>\d+)/$',
        sm_views.ViewTeacherProfile.as_view(),
        name='teacher_profile'),

    url(r'staff/create/$', sm_views.CreateStaff.as_view(),
        name='create_staff'),

    url(r'staff/(?P<staff_id>\d+)/$',
        sm_views.UpdateStaff.as_view(),
        name='update_staff'),

    url(r'staff/delete/(?P<staff_id>\d+)/$',
        sm_views.DeleteStaff.as_view(),
        name='delete_staff'),

    url(r'staff/upload/$',
        sm_views.UploadStaff.as_view(),
        name='upload_staff'),

    url(r'staff/profile/(?P<teacher_id>\d+)/$',
        sm_views.ViewStaffProfile.as_view(),
        name='staff_profile'),

    url(r'staff/$',
        sm_views.StaffManagement.as_view(),
        name='staff_management'),


]