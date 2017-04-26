from django.conf.urls import url
from django.contrib import admin

from communication_management import views as cm_views

urlpatterns = [

    url(r'my/$',
        cm_views.GetMyNotifications.as_view(),
        name='get_my_notifications'),

    url(r'notification_board/$',
        cm_views.NotificationBoard.as_view(),
        name='notification_board'),

    url(r'view/(?P<notification_id>\d+)/$',
        cm_views.ViewNotification.as_view(),
        name='view_notification'),
]