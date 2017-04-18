# Create your models here.
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common import choices
from common.choices import STATUS_CHOICES as status_choices
from user.models import User

class Notice(models.Model):
    """
    """
    text = models.TextField(null=False, verbose_name=_("text"), blank=False)
    #created_by = models.ForeignKey(sm_staff)
    creted_on = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    is_published = models.BooleanField(default=False, blank=False)
    status = models.CharField(default=choices.STATUS_TYPE_ACTIVE, null=False,
        choices=status_choices, verbose_name=_("status"), blank=False,max_length=1)

    class Meta:
        db_table = "nb_notice"
    
class NoticeUserMap(models.Model):
    """
    """
    notice = models.ForeignKey(Notice, null=False, unique=True, blank=False)
    user = models.ForeignKey(User, null=False, unique=True, blank=False)

    class Meta:
        db_table = "nb_notice_user_map"