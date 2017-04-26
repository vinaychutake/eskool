from django.conf.urls import url
from django.contrib import admin

from communication_management import views as cm_views

urlpatterns = [
    url(r'template/create/$', cm_views.CreateNotificationTemplate.as_view(),
        name='create_notification_template'),

    url(r'template/(?P<notification_template_id>\d)/$',
        cm_views.UpdateNotificationTemplate.as_view(),
        name='update_notification_template'),

    url(r'template/delete/(?P<notification_template_id>\d)/$',
        cm_views.DeleteNotificationTemplate.as_view(),
        name='delete_notification_template'),

    url(r'templates/$',
        cm_views.GetNotificationTemplates.as_view(),
        name='get_notification_templates'),

    url(r'create/$', cm_views.CreateNotification.as_view(),
        name='create_notification'),

    url(r'(?P<notification_id>\d)/$',
        cm_views.UpdateNotification.as_view(),
        name='update_notification'),

    url(r'delete/(?P<notification_id>\d)/$',
        cm_views.DeleteNotification.as_view(),
        name='delete_notification'),

    url(r'^$',
        cm_views.GetMyNotifications.as_view(),
        name='get_my_notifications'),

    # url(r'^list/$',
    #     cm_views.ListNotifications.as_view(),
    #     name='list_notifications'),

    url(r'^notification_board/$',
        cm_views.NotificationBoard.as_view(),
        name='notification_board'),

    url(r'view/(?P<notification_id>\d+)/$',
        cm_views.ViewNotification.as_view(),
        name='view_notification'),
]