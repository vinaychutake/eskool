"""
API module for communication management
This apis can be accessed from any application
"""
from models import NotificationTemplate, Notification
from common.utils import paginate_objects
def create_notification_template(name, code, template, config):
    """
    creates new template
    """
    obj_notification_temp = NotificationTemplate(name=name,
                                                 code=code,
                                                 template=template,
                                                 config=config)
    try:
        obj_notification_temp.clean()
        obj_notification_temp.save()
    except Exceptions as e:
        print e , "error while creating obj"

def update_notification_template(template_obj, name, code, template, config):
    """
    Updates given notification template with given data
    """
    template_obj.update(name=name, 
                        code=code,
                        template=template,
                        config=config)
    try:
        template_obj.clean()
    except Exceptions as e:
        print "error while updating notification_template"

def get_notification_templates():
    """
    Returns all notfications templates which are active in json format
    """
    objs = NotificationTemplate.objects.filter(status='A')
    return objs

def delete_notification_template(template_obj):
    """
    Deletes given notification template
    """
    template_obj.delete()
    pass

def get_notification_template_obj(template_id):
    """
    Returns notification template object with given id
    """
    obj = NotificationTemplate.objects.get(id=template_id)
    return obj

def get_notification_obj(notification_id):
    """
    Returns notification object with given id
    """
    obj = Notification.objects.get(id=notification_id)
    return obj

def create_notifition(template, receivers, text_data):
    """
    Create new notification object
    Params:
        template: Object of template class
        receivers: List of receivers/ user objects
        data: Actual data to send in json format
    """
    for receiver in receivers:
        Notification.objects.bulk_create([
                Notification(template=template,
                             eceiver=receiver,
                             text=text_data)]
    pass

def update_notifition(notification_obj, text_data):
    """
    Create new notification object
    Params:
        notification: Object of notification class
        receivers: List of receivers/ user objects
        data: Actual data to send in json format
    """
    notification_obj.update(text=text_data)
    try:
        notification_obj.clean()
    except Exceptions as e:
        print "error while modifying notification"
    pass

def delete_notification(notification):
    """
    Deletes given notification
    """
    notification.delete()
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
    notifications = Notification.objects.filter(receiver=user)
    if paginate:
        notifications = paginate_objects(objs, 5, page_no)
    return {'notifications':notifications}
    # Use paginate_objects method from common.utils to get the list of objects

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
