"""
API module for notice board
This apis can be accessed from any application
"""

def create_notice(creator, group_names, text):
	"""
	Creates new notice
	Params:
		creator: user object who is creating this notice
		group_names: List of group names
		text: Actual notice text
	"""

	pass


def get_notices(user, num_of_records=10):
	"""
	Returns notices for given user
	Params:
		user: User Object
		num_of_records: Number of notices to return
	Returns:
		Notices in json format
	"""

	#Find groups for given user and the find notices for that groups
	pass

def publish_notice(notice, send_notification=False):
	"""
	Publishes the given notice
	Params:
		notice: Notice object
		send_notification: Boolean. Weather to send email/sms notification
	"""

	pass