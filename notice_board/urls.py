from django.conf.urls import url
from django.contrib import admin

from notice_board import views as notice_views

urlpatterns = [

    url(r'create/$', notice_views.CreateNotice.as_view(), name='create_notice'),

    url(r'update/(?P<notice_id>\d+)/$', notice_views.UpdateNotice.as_view(), name='update_notice'),

    url(r'delete/(?P<notice_id>\d+)/$', notice_views.DeleteNotice.as_view(), name='delete_notice'),

    url(r'publish/(?P<notice_id>\d+)/$', notice_views.PublishNotice.as_view(), name='publish_notice'),

	url(r'view/(?P<notice_id>\d+)/$', notice_views.ViewNotice.as_view(), name='view_notice'),

    url(r'my/$', notice_views.GetMyNotices.as_view(), name='my_notices'),

    url(r'list/$', notice_views.ListNotices.as_view(), name='list_notices'),

    url(r'notice_board/$', notice_views.NoticeBoard.as_view(), name='notice_board'),
]