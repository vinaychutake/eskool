from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin

from common import choices


class State(models.Model):
    name = models.CharField(max_length = 80, unique = True)
    code = models.CharField(max_length=16, unique = True)
    status = models.CharField(max_length=1, choices = choices.STATUS_CHOICES, default = choices.STATUS_TYPE_ACTIVE)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length = 80, unique = True)
    state = models.ForeignKey(State, related_name="cities")
    status = models.CharField(max_length=1, choices = choices.STATUS_CHOICES, default = choices.STATUS_TYPE_ACTIVE)

    def __unicode__(self):
        return self.name


class Address(models.Model):
    address1 = models.CharField(max_length = 80)
    address2 = models.CharField(max_length = 80)
    address3 = models.CharField(max_length = 80)
    city = models.ForeignKey(City, related_name="addresses")
    status = models.CharField(max_length=1, choices = choices.STATUS_CHOICES, default = choices.STATUS_TYPE_ACTIVE)

    def __unicode__(self):
        return self.address1


class ContactNumber(models.Model):
    contact_number = models.CharField(max_length = 80, unique = True)
    status = models.CharField(max_length=1, choices = choices.STATUS_CHOICES, default = choices.STATUS_TYPE_ACTIVE)

    def __unicode__(self):
        return self.contact_number


class Cast(models.Model):
    name = models.CharField(max_length = 80, unique = True)
    code = models.CharField(max_length=16, unique = True)
    status = models.CharField(max_length=1, choices = choices.STATUS_CHOICES, default = choices.STATUS_TYPE_ACTIVE)


class Institute(TenantMixin):
    name = models.CharField(max_length=80, unique = True)
    code = models.CharField(max_length=48, unique = True)
    sub_domain = models.CharField(max_length=48, unique = True)
    logo = models.ImageField(max_length=500, blank = True, null=True, 
                                    upload_to="logos")
    type = models.CharField(max_length=20, choices = choices.INSTITUTE_TYPE_CHOICES, default = choices.INSTITUTE_TYPE_APPLICATION)
    address = models.ForeignKey(Address, related_name = "institutes")
    status = models.CharField(max_length=1, choices = choices.STATUS_CHOICES, default = choices.STATUS_TYPE_ACTIVE)

    def __unicode__(self):
        return self.name

