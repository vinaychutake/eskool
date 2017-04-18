"""
database definations
"""
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.choices import STATUS_CHOICES as status_choices

class EmailTemplate(models.Model):
    """
    email template database definations having
    name, template and status
    """
    name = models.CharField(max_length=48, unique=True,
    	verbose_name=_("name"))
    template = models.TextField(null=False,
        verbose_name=_("template"))
    status = models.CharField(default='A', null=False,
        choices=status_choices, verbose_name=_("status"))
    class Meta:
        db_table = "cm_email_template"
    def __str__(self):
        return str(self.name)

class SmsTemplate(models.Model):
    """
    sms template database
    """
    name = models.CharField(max_length=48, unique=True,
        verbose_name=_("name"))
    template = models.TextField(null=False,
        verbose_name=_("template"))
    status = models.CharField(default='A', null=False,
        choices=status_choices, verbose_name=_("status"))
    class Meta:
        db_table = "cm_sms_template"
    def __str__(self):
        return str(self.name)

class EmailNotificationQueue(models.Model):
    """
    database to send email notification
    """
    data = models.TextField(null=False)
    mail_to = models.CharField(max_length=255, null=False)
    email_template = models.ForeignKey(EmailTemplate)
    sent_at = models.DateTimeField(null=True,
        verbose_name=_("sent_at"))
    status = models.CharField(default='A', null=False,
        choices=status_choices, verbose_name=_("status"))
    class Meta:
        db_table = "cm_email_notification_queue"
    def __str__(self):
        return str(self.mail_to)

class SmsNotificationQueue(models.Model):
    """
    database to send sms notification
    """
    data = models.TextField(max_length=300, null=False)
    phone_num = models.CharField(null=False) #- validaters ?
    sms_template = models.ForeignKey(SmsTemplate)
    sent_at = models.DateTimeField(null=True,
        verbose_name=_("sent_at"))
    status = models.CharField(default='A', null=False,
        choices=status_choices, verbose_name=_("status"))
    class Meta:
        db_table = "cm_sms_notification_queue"
    def __str__(self):
        return str(self.phone_num)
