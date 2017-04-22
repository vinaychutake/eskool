"""
Contains all common models of project
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from common import choices


class SoftDeleteMixin(models.Model):
    """
    Soft delete mixin class. Make sure model has status field before inheriting this class
    """

    def delete(self, *args, **kwargs):
        """
        Overridden delete method to update status to D
        """

        self.status = 'D'
        self.save()

    class Meta:
        abstract = True

class StatusMixin(SoftDeleteMixin):
    """
    Mixin class for a status field. All models which have status
    field should inherit these
    """

    status = models.CharField(max_length=1, choices=choices.STATUS_CHOICES,
                              default=choices.STATUS_TYPE_ACTIVE)

    class Meta:
        abstract = True

