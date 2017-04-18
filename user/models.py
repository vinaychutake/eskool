# Create your models here.
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from common.choices import STATUS_CHOICES as status_choices
from common.choices import GENDER_CHOICES as gender_choices
from common.choices import CONTACT_CHOICES as contact_choices

USER_IMAGES_PATH = '/media'

class User(AbstractUser):
    """
    """
    first_name = models.CharField(max_length=48, null=False, blank=False)
    middle_name = models.CharField(max_length=48, null=True, blank=True)
    last_name = models.CharField(max_length=48, null=False, blank=False)
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to=USER_IMAGES_PATH, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    gender = models.CharField(default='A', null=False,
        choices=gender_choices, verbose_name=_("gender"), blank=False)
    is_deleted = models.BooleanField(default=False)
    #cast = models.ForeignKey(tm_cast, null=False, unique=True, blank=False)
    class Meta:
        db_table = "am_user"

    def __str__(self):
        return str(self.first_name) 

class UserAddressMap(models.Model):
    """
    """
    user = models.ForeignKey(User, null=False, blank=False)
    #address = models.ForeignKey(tm_address, null=False, blank=False)
    class Meta:
        db_table = "am_user_address_map"


class UserContactMap(models.Model):
    """
    """
    #contact_num = models.ForeignKey(tm_contact_number, null=False, blank=False)
    type = models.CharField(null=False,
        choices=contact_choices, verbose_name=_("type"), blank=False)

    class Meta:
        db_table = "am_user_address_map"
