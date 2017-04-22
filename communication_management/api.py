"""
API module for communication management
This apis can be accessed from any application
"""

def create_email_template(name, template_structure):
	"""
	creates new email template
	"""

	pass

def create_sms_template(name, template_structure):
	"""
	creates new sms template
	"""

	pass

def create_email_notifition(template, receivers, data):
	"""
	Create new email notification
	Params:
		template: Object of email_template class
		receivers: List of receivers email addresses
		data: Actual data to send in json format
	"""

	#Need to substitute data into the template
	#Create objects in bulk
	pass

def create_sms_notifition(template, receivers, data):
	"""
	Create new email notification
	Params:
		template: Object of sms_template class
		receivers: List of receivers phone numbers
		data: Actual data to send in json format
	"""

	#Need to substitute data into the template
	#Create objects in bulk
	pass


def send_email_notification(institute, email_notification):
	"""
	Sends actual email notification
	Params:
		institute: institute object
		email_notification: email_notification object 	
	"""

	#Send email notification
	pass

def send_sms_notification(institute, sms_notification):
	"""
	Sends actual email notification
	Params:
		institute: institute object
		sms_notification: sms_notification object 	
	"""

	#Send sms notification
	pass
