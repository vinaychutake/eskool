from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from api import *
from models import NotificationTemplate, Notification

class CreateNotificationTemplate(View):
    """
    """

    def post(self, request):
        """
        """
        name = request.POST.get("name","")
        code = request.POST.get("code","")
        template = request.POST.get("template","")
        config = request.POST.get("config","")
        create_notification_template(name,
                                     code,
                                     template,
                                     config)

class UpdateNotificationTemplate(View):
    """
    """

    def post(self, request, notification_template_id):
        """
        """
        name = request.POST.get("name","")
        code = request.POST.get("code","")
        template = request.POST.get("template","")
        config = request.POST.get("config","")
        update_notification_template(name,
                                     code,
                                     template,
                                     config)

class DeleteNotificationTemplate(View):
    """
    """

    def post(self, request, notification_template_id):
        """
        """
        template_obj = NotificationTemplate(id=notification_template_id)
        delete_notification_template(template_obj)

class GetNotificationTemplates(View):
    """
    """

    def get(self, request):
        """
        """
        get_notification_templates()

class CreateNotification(View):
    """
    """

    def post(self, request):
        """
        """
        template = request.POST.get("template", '')
        receivers = request.POST.get("receivers", '')
        text_data = request.POST.get("text_data", '')
        create_notifition(template, receivers, text_data)

class UpdateNotification(View):
    """
    """

    def post(self, request, notification_id):
        """
        """
        notification_obj = Notification(id=notification_id)
        text_data = request.POST.get("data",'')
        update_notifition(notification_obj, text_data)

class DeleteNotification(View):
    """
    """

    def post(self, request, notification_id):
        """
        """
        notification_obj = Notification(id=notification_id)
        delete_notification(notification_obj)

class GetMyNotifications(View):
    """
    """

    def get(self, request):
        """
        """
        user = request.user
        page_no = 1#int(request.GET.get('start'))
        notifications = get_user_notifications(user, paginate=True)

        data = []
        for index, notifications in enumerate(notifications.get('notifications', [])):
            notification = [index+1,
                      "<a href=%s>%s</a>" %(reverse('view_notification',
                                                    kwargs={'notification_id': notifications.id}),
                                            notifications.template),
                      "%s ..." %(notifications.text[:30])]
            data.append(notification)

        response = {'data': data}

        return JsonResponse(response)

class ListNotifications(View):
    """
    """

    def get(self, request):
        """
        """
        user = request.user
        page_no = 1#int(request.GET.get('start'))
        notifications = get_user_notifications(user, paginate=True)

        data = []
        for index, notifications in enumerate(notifications.get('notifications', [])):
            notification = [index+1,
                      "<a href=%s>%s</a>" %(reverse('view_notification',
                                                    kwargs={'notification_id': notifications.id}),
                                            notifications.template),
                      "%s ..." %(notifications.text[:30])]
            data.append(notification)

        response = {'data': data}

        return JsonResponse(response)

class NotificationBoard(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "notification_base.html")

class ViewNotification(View):
    """
    """

    def get(self, request, notification_id):
        """
        """

        try:
            notifications = get_notification_obj(notification_id)
            print "***********notifications***************",notifications
            return render(request, 'view_notification.html', {'notice': notifications})
        except ObjectDoesNotExist:
            raise Http404