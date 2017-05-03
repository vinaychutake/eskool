from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group

from staff_management.models import StaffType

@receiver(post_save, sender=StaffType)
def staff_created_signal(sender, **kwargs):
    if kwargs.get('created', False):
    	type_name = kwargs.get('instance')
        group = Group(name = type_name)
        group.save()
