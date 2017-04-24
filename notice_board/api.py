"""
API module for notice board
This apis can be accessed from any application
"""
from common.utils import paginate_objects
from notice_board.models import Notice

def create_notice(name, creator, group_names, text):
    """
    Creates new notice
    Params:
        creator: user object who is creating this notice
        group_names: List of group names
        text: Actual notice text
    """
    notice = Notice(name=name,
                                   text=text,
                                   creator=creator)
    groups_list = Group.object.all(name__in=group_names)
    notice.groups.set(groups_list)
    notice.clean()
    notice.save()

def update_notice(notice_id, group_names, text):
    """
    Creates new notice
    Params:
        notice_id: notice id which is going to be updated
        group_names: List of group names
        text: Actual notice text
    """
    notice = get_notice_obj(notice_id)
    groups_list = Group.object.filter(name__in=group_names)
    notice.groups.set(groups_list)
    notice.text = text
    notice.clean()
    notice.save()

def get_user_notices(user, page_no=1, paginate=True):
    """
    Returns notices for given user
    Params:
        user: User Object
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    Returns:
        Notices in json format
    """
    notices = Notice.objects.filter(groups__id__in=user.groups.all().values_list('id', flat=True), 
                                    status='A')
    if paginate:
        notices = paginate_objects(notices, 5, page_no)
    return {'notices' : notices}

def get_notices(creator, return_all=False, page_no=1, paginate=True):
    """
    Returns notices to edit
    Params:
        creator: User object
        return_all: weather to apply creator filter or not
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """
    if return_all:
        notices = Notice.objects.filter(creator=creator, status='A')
    else:
        notices = Notice.objects.all()
    if paginate:
        notices = paginate_objects(notices, 5, page_no)
    return notices

def publish_notice(notice_id):
    """
    Publishes the given notice
    Params:
        notice_id: Notice id
        send_notification: Boolean. Weather to send email/sms notification
    """
    notice = get_notice_obj(notice_id)
    notice.is_published = True
    notice.clean()
    notice.save()


def delete_notice(notice_id):
    """
    Returns the notice object with given id
    Params:
        notice_id : Notice id
    """
    notice = get_notice_obj(notice_id)
    notice.delete()

def get_notice_obj(notice_id):
    """
    Returns the notice object with given id
    Params:
        notice_id : Notice id
    """
    notice = Notice.objects.get(id=notice_id)
    return notice
