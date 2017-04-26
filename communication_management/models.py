"""
database definations
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from common.choices import NOTIFICATION_ACTIVE, NOTIFICATION_CHOICES as notification_choices
from common.models import StatusMixin, SoftDeleteMixin

class NotificationTemplate(StatusMixin):
    """
    template database definations having 
    name, template and status
    """

    name = models.CharField(max_length=48, unique=True, verbose_name=_("name"))

    code = models.CharField(max_length=16, unique=True, verbose_name=_('code'))

    template = models.TextField(null=False, verbose_name=_("template"))

    config = models.TextField(null=True)

    template_type = models.CharField(max_length=1, null=False, default='A')

    class Meta:
        db_table = "cm_notification_template"

    def __str__(self):
            return self.name

class Notification(SoftDeleteMixin):
    """
    database to send notification
    """

    text = models.TextField(null=False)

    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='notifications')

    template = models.ForeignKey(NotificationTemplate, related_name='notifications')

    is_sent = models.BooleanField(default=False)

    sent_at = models.DateTimeField(null=True, verbose_name=_("sent_at"))

    status = models.CharField(max_length=1, default=NOTIFICATION_ACTIVE, null=False,
                              choices=notification_choices, verbose_name=_("status"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_notifications')

    class Meta:
        db_table = "cm_notification"

    def __str__(self):
        return self.text
    