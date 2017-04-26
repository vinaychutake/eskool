from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from api import *
from models import NotificationTemplate, Notification

# class GetMyNotifications(View):
#     """
#     """

#     def get(self, request):
#         """
#         """
#         user = request.user
#         page_no = 1#int(request.GET.get('start'))
#         notifications = get_user_notifications(user, paginate=True)
#         notification_count = notifications['count']
#         data = []
#         for index, notifications in enumerate(notifications.get('notifications', [])):
#             notification = [index+1,
#                       "<a href=%s>%s</a>" %(reverse('view_notification',
#                                                     kwargs={'notification_id': notifications.id}),
#                                             notifications.template),
#                       "%s ..." %(notifications.text[:30])]
#             data.append(notification)

#         response = {'recordsTotal': notification_count,
#                     'data': data, 'recordsFiltered': notification_count}

#         return JsonResponse(response)

class GetMyNotifications(View):
    """
    """
    def get(self, request):
        user = request.user
        notifications = get_user_notifications(user, paginate=False)
        return render(request, "pages-timeline.html")


class NotificationBoard(View):
    """
    """

    def get(self, request):
        """
        """
        print "****************here*****************"
        user = request.user
        notifications = get_user_notifications(user, paginate=False)
        return render(request, "pages-timeline.html", {'notifications':notifications})
        #return render(request, "notification_base.html")

class ViewNotification(View):
    """
    """

    def get(self, request, notification_id):
        """
        """
        try:
            notifications = get_notification_obj(notification_id)
            return render(request, 'view_notification.html', {'notifications': notifications})
        except ObjectDoesNotExist:
            raise Http404