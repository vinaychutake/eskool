from __future__ import unicode_literals

from django.apps import AppConfig

class StaffManagementConfig(AppConfig):
    name = 'staff_management'

    def ready(self):
        from .auth_management.signal_receiver import staff_created_signal
