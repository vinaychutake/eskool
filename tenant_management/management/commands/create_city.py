from django.core.management import BaseCommand
from django.db import IntegrityError
from tenant_management.city_list import city_list
from tenant_management.models import State,City
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# A command must define handle()
	def handle(self, *args, **options):
		for city in city_list:
			state = State.objects.get(code=city['code'])
			City.objects.get_or_create(name=city['name'],
                    state=state)
		self.stdout.write("City Created Successfully!")
