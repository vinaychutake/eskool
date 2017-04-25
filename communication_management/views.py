from django.shortcuts import render
from django.views.generic import View
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
        notifications = get_user_notifications(user)
        return render(request, 'tets.html', {'user_notification':notifications})

class ListNotifications(View):
    """
    """

    def get(self, request):
        """
        """
        pass
