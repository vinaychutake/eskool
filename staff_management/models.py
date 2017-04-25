from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from common.models import StatusMixin

class StaffType(StatusMixin):
    """
    Class representing an type of staff. e.g. teachers, accountant, peon
    """

    name = models.CharField(_('Name'), max_length=48, unique=True, null=False,
                            blank=False)

    code = models.CharField(_('Code'), max_length=16, unique=True, null=False,
                            blank=False)

    staff_type = models.CharField(_('Staff Type'), max_length=2, null=False,
                                  blank=False, default='A')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sm_staff_type'

class Staff(models.Model):
    """
    Class representing an staff person
    """

    staff_type = models.ForeignKey(StaffType, related_name='staffs')

    joining_date = models.DateField(_('Joining Date'), null=False, blank=False)

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    reporting_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='team')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = 'sm_staff'

class Teacher(models.Model):
    """
    Class representing a teacher
    """

    staff = models.OneToOneField(Staff)

    def __str__(self):
        return self.staff.user.get_full_name()

    class Meta:
        db_table = 'sm_teacher'
    