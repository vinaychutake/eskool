from django.dispatch import receiver
from django.db.models.signals import post_save
from staff_management.models import StaffType
from django.contrib.auth.models import Group

@receiver(post_save, sender=StaffType)
def staff_created_signal(sender, **kwargs):
    if kwargs.get('created', False):
    	type_name = kwargs.get('instance')
        print "staff type is created"
        group = Group(name = type_name)
        group.save()
