from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from common.choices import GENDER_CHOICES as gender_choices

from tenant_management.models import Address, ContactNumber

class User(AbstractUser):
    """
    Class Representing an student/teacher/staff/admin
    """

    middle_name = models.CharField(max_length=48, null=True, blank=True)

    birth_date = models.DateTimeField(null=True, blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    gender = models.CharField(max_length=1, null=False, choices=gender_choices,
                              verbose_name=_("gender"), blank=False)

    is_deleted = models.BooleanField(default=False)

    addresses = models.ManyToManyField(Address)

    contace_numbers = models.ManyToManyField(ContactNumber)

    class Meta:
        db_table = "am_user"

    def __str__(self):
        """
        """

        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """

        full_name = "%s %s %s (%s)" %(self.first_name, self.middle_name, self.last_name, self.username)
        return full_name.strip()