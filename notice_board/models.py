from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group

from common.models import StatusMixin
from eskool.settings import AUTH_USER_MODEL
from common.choices import STATUS_TYPE_ACTIVE, STATUS_CHOICES as status_choices

class Notice(StatusMixin):
    """
    Class representing an notice
    """

    name = models.CharField(null=False, max_length=48)

    text = models.TextField(null=False, verbose_name=_("text"), blank=False)
    
    creator = models.ForeignKey(AUTH_USER_MODEL, related_name='notices')

    creted_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    
    is_published = models.BooleanField(default=False, blank=False)

    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "nb_notice"
        ordering = ['-creted_on']