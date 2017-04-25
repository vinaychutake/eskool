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
    obj_notification_temp.clean()
    obj_notification_temp.save()

def update_notification_template(template_obj, name, code, template, config):
    """
    Updates given notification template with given data
    """
    template_obj.name=name, 
    template_obj.code=code,
    template_obj.template=template,
    template_obj.config=config
    template_obj.clean()
    template_obj.save()

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


def get_notification_template_obj(template_id):
    """
    Returns notification template object with given id
    """
    return NotificationTemplate.objects.get(id=template_id)

def get_notification_obj(notification_id):
    """
    Returns notification object with given id
    """

    return Notification.objects.get(id=notification_id)

def create_notifition(template, receivers, text_data):
    """
    Create new notification object
    Params:
        template: Object of template class
        receivers: List of receivers/ user objects
        data: Actual data to send in json format
    """

    notifications = []
    for receiver in receivers:
        notifications.append(Notification(template=template,
                                          receiver=receiver,
                                          text=text_data))

    Notification.objects.bulk_create(notifications)

def update_notifition(notification_obj, text_data):
    """
    Create new notification object
    Params:
        notification: Object of notification class
        receivers: List of receivers/ user objects
        data: Actual data to send in json format
    """

    notification_obj.text=text_data
    notification_obj.clean()
    notification_obj.save()

def delete_notification(notification_obj):
    """
    Deletes given notification
    """
    notification_obj.delete()


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
        notifications = paginate_notifications(paginate, notifications, 5, page_no)
    return notifications

def paginate_notifications(paginate, notifications, records_per_page, page_no):
    """
    """
    count = len(notifications)
    if paginate:
        notifications = paginate_objects(notifications, records_per_page, page_no)
    return {'notifications': notifications, 'count': count, 'returned_count': len(notifications)}

