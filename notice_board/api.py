"""
API module for notice board
This apis can be accessed from any application
"""

from common.utils import paginate_objects
from notice_board.models import Notice
from django.contrib.auth.models import Group

def create_notice(name, creator, groups, text):
    """
    Creates new notice
    Params:
        creator: user object who is creating this notice
        group_names: List of group names
        text: Actual notice text
    """

    notice = Notice(name=name,
                    text=text,
                    creator=creator,
                    groups=groups)
    notice.clean()
    notice.save()

def update_notice(notice_id, name, groups, text):
    """
    Creates new notice
    Params:
        notice_id: notice id which is going to be updated
        group_names: List of group names
        text: Actual notice text
    """

    notice = get_notice_obj(notice_id)
    notice.groups = groups
    notice.name = name
    notice.text = text
    notice.clean()
    notice.save()

def get_user_notices(user, page_no=1, paginate=True, records_per_page=10):
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

    return paginate_notices(paginate, notices, records_per_page, page_no)

def get_notices(creator, return_all=False, page_no=1, paginate=True, records_per_page=10):
    """
    Returns notices to edit
    Params:
        creator: User object
        return_all: weather to apply creator filter or not
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """
    if return_all:
        notices = Notice.objects.filter(status='A')
    else:
        notices = Notice.objects.filter(creator=creator, status='A')

    return paginate_notices(paginate, notices, records_per_page, page_no)

def paginate_notices(paginate, notices, records_per_page, page_no):
    """
    """
    count = len(notices)
    if paginate:
        notices = paginate_objects(notices, records_per_page, page_no) 
    return {'notices': notices, 'count': count, 'returned_count': len(notices)}

def publish_notice(notice_id):
    """
    Publishes the given notice
    Params:
        notice_id: Notice id
    """
    notice = get_notice_obj(notice_id)
    if notice.is_published:
        notice.is_published = False
    else:
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
