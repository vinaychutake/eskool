"""
database definations
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.choices import NOTIFICATION_ACTIVE, NOTIFICATION_CHOICES as notification_choices
from common.models import StatusMixin, SoftDeleteMixin

class EmailTemplate(StatusMixin):
    """
    email template database definations having
    name, template and status
    """

    name = models.CharField(max_length=48, unique=True, verbose_name=_("name"))

    template = models.TextField(null=False, verbose_name=_("template"))

    class Meta:
        db_table = "cm_email_template"

    def __str__(self):
        return self.name

class SmsTemplate(StatusMixin):
    """
    sms template database
    """

    name = models.CharField(max_length=48, unique=True, verbose_name=_("name"))

    template = models.TextField(null=False, verbose_name=_("template"))

    class Meta:
        db_table = "cm_sms_template"

    def __str__(self):
        return self.name

class EmailNotification(SoftDeleteMixin):
    """
    database to send email notification
    """

    data = models.TextField(null=False)

    mail_to = models.EmailField(max_length=255, null=False)

    email_template = models.ForeignKey(EmailTemplate, related_name='emails')

    sent_at = models.DateTimeField(null=True, verbose_name=_("sent_at"))

    status = models.CharField(max_length=1, default=NOTIFICATION_ACTIVE, null=False,
                              choices=notification_choices, verbose_name=_("status"))

    class Meta:
        db_table = "cm_email_notification"

    def __str__(self):
        return self.mail_to

class SmsNotification(SoftDeleteMixin):
    """
    database to send sms notification
    """

    data = models.TextField(max_length=300, null=False)

    phone_number = models.CharField(max_length=20,null=False)

    sms_template = models.ForeignKey(SmsTemplate, related_name='all_sms')

    sent_at = models.DateTimeField(null=True, verbose_name=_("sent_at"))

    status = models.CharField(max_length=1, default=NOTIFICATION_ACTIVE, null=False,
                              choices=notification_choices, verbose_name=_("status"))

    class Meta:
        db_table = "cm_sms_notification"

    def __str__(self):
        return self.phone_number
