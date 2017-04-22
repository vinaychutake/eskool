from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tenant_schemas.models import TenantMixin

from common import choices
from common.models import StatusMixin, SoftDeleteMixin

class State(StatusMixin):
    """
    Class representing a state. e.g. Maharashtra
    """

    name = models.CharField(max_length=80, unique=True, null=False, blank=False)

    code = models.CharField(max_length=16, unique=True, null=False, blank=False)

    def __str__(self):

        return self.name

    class Meta:
        db_table = 'tm_state'

class City(StatusMixin):
    """
    Class representing a city which belongs to a particular state
    """

    name = models.CharField(max_length=80, unique=True, null=False, blank=False)

    state = models.ForeignKey(State, related_name="cities", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tm_city'
        verbose_name_plural = _('Cities')
        unique_together = ('name', 'state')

class Address(StatusMixin):
    """
    Class representing an address
    """

    address1 = models.CharField(max_length=80, null=False, blank=False)

    address2 = models.CharField(max_length=80, null=True, blank=True)

    address3 = models.CharField(max_length=80, null=True, blank=True)

    city = models.ForeignKey(City, related_name="addresses", null=False, blank=False)

    def __str__(self):
        return self.address1

    class Meta:
        db_table = 'tm_address'

class ContactNumber(StatusMixin):
    """
    class Representing an contact number
    """

    contact_number = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.contact_number

    class Meta:
        db_table = 'tm_contact_number'

class Institute(TenantMixin):
    """
    Class representing an institute
    """

    name = models.CharField(max_length=80, unique=True, null=False, blank=False)

    code = models.CharField(max_length=48, unique=True, null=False, blank=False)

    logo = models.ImageField(blank=True, null=True, upload_to="logos")

    institute_type = models.CharField(max_length=1, choices=choices.INSTITUTE_TYPE_CHOICES, 
                                      default=choices.INSTITUTE_TYPE_APPLICATION)

    address = models.ForeignKey(Address, related_name="institutes", null=True, blank=True)

    status = models.CharField(max_length=1, choices=choices.STATUS_CHOICES,
                              default=choices.STATUS_TYPE_ACTIVE)

    @property
    def is_system(self):
        return self.institute_type == 'S'

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tm_institute'
