from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from notice_board import views as notice_views

urlpatterns = [

    url(r'create/$',
    	login_required(notice_views.CreateNotice.as_view()),
    	name='create_notice'),

    url(r'update/(?P<notice_id>\d+)/$',
    	login_required(notice_views.UpdateNotice.as_view()),
    	name='update_notice'),

    url(r'delete/(?P<notice_id>\d+)/$',
    	login_required(notice_views.DeleteNotice.as_view()),
    	name='delete_notice'),

    url(r'publish/(?P<notice_id>\d+)/$',
    	login_required(notice_views.PublishNotice.as_view()),
    	name='publish_notice'),

	url(r'view/(?P<notice_id>\d+)/$',
		login_required(notice_views.ViewNotice.as_view()),
		name='view_notice'),

    url(r'my/$',
    	login_required(notice_views.GetMyNotices.as_view()),
    	name='my_notices'),

    url(r'manage/$',
    	login_required(notice_views.ManageNotices.as_view()),
    	name='manage_notices'),

    url(r'notice_board/$',
    	login_required(notice_views.NoticeBoard.as_view()),
    	name='notice_board'),
]