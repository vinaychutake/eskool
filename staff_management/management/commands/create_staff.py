from django.core.management import BaseCommand
from django.db import IntegrityError
from staff_management.staff_config import staff_type_list
from staff_management.models import StaffType
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# A command must define handle()
	def handle(self, *args, **options):
		for staff_type in staff_type_list:
			StaffType.objects.get_or_create(name=staff_type['name'],
                    code=staff_type['code'],
                    staff_type=staff_type['type'])
		self.stdout.write("Staff Created Successfully!")
