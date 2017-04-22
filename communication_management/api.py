"""
API module for communication management
This apis can be accessed from any application
"""

def create_notification_template(name, code, template_structure, config):
    """
    creates new template
    """
    #Before creating object, call clean method and handle exceptions
    pass

def update_notification_template(template, name, code, template_structure, config):
    """
    Updates given notification template with given data
    """
    #Before updating object, call clean method and handle exceptions
    pass

def get_notification_templates():
    """
    Returns notfications templates in json format
    """
    pass

def delete_notification_template(template):
    """
    Deletes given notification template
    """
    pass

def get_notification_template_obj(template_id):
    """
    Returns notification template object with given id
    """
    pass

def get_notification_obj(notification_id):
    """
    Returns notification object with given id
    """
    pass

def create_notifition(template, receivers, data):
    """
    Create new notification object
    Params:
        template: Object of template class
        receivers: List of receivers/ user objects
        data: Actual data to send in json format
    """

    #Need to substitute data into the template
    #Create objects in bulk
    #Before creating object, call clean method and handle exceptions
    pass

def update_notifition(notification, receivers, data):
    """
    Create new notification object
    Params:
        notification: Object of notification class
        receivers: List of receivers/ user objects
        data: Actual data to send in json format
    """

    #you can not update template of notifications
    #Need to substitute data into the template
    #update objects in bulk
    #Before updating object, call clean method and handle exceptions
    pass

def delete_notification(notification):
    """
    Deletes given notification
    """
    pass

def send_notification(institute, notification):
    """
    Sends actual notification
    Params:
        institute: institute object
        notification: notification object   
    """

    # Take desision weahter to send email of sms
    # Need to check weather institute has sms enabled
    # and institude has purchased sms / email module
    #Send notification
    pass

def get_user_notifications(user, page_no=1, paginate=True):
    """
    Returns notifications for given user
    Params:
        user: User Object
        page_no: page number
        paginate: If False return all objects, else return objects on given page
    Returns:
        Notifications in json format
    """

    # Use paginate_objects method from common.utils to get the list of objects
    pass

def list_notifications(creator, return_all=False, page_no=1, paginate=True):
    """
    Returns notifications to edit
    Params:
        creator: User object
        return_all: weather to apply creator filter or not
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """
    pass
