from django.core.management import BaseCommand
from django.db import IntegrityError
from tenant_management.state_list import state_list
from tenant_management.models import State
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# A command must define handle()
	def handle(self, *args, **options):
		for state in state_list:
			State.objects.get_or_create(name=state['name'],
                    code=state['code'])
		self.stdout.write("State Created Successfully!")
