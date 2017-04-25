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
        pass


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
        pass

class DeleteNotificationTemplate(View):
    """
    """

    def post(self, request, notification_template_id):
        """
        """
        template_obj = NotificationTemplate(id=notification_template_id)
        delete_notification_template(template_obj)
        pass

class GetNotificationTemplates(View):
    """
    """

    def get(self, request):
        """
        """
        get_notification_templates()
        pass

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
        pass

class UpdateNotification(View):
    """
    """

    def post(self, request, notification_id):
        """
        """
        
        pass

class DeleteNotification(View):
    """
    """

    def post(self, request, notification_id):
        """
        """
        pass

class GetMyNotifications(View):
    """
    """

    def get(self, request):
        """
        """
        pass

class ListNotifications(View):
    """
    """

    def get(self, request):
        """
        """
        pass
