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

def update_notice(notice, group_names, text):
    """
    Creates new notice
    Params:
        notice: notice object which is going to be updated
        group_names: List of group names
        text: Actual notice text
    """

    pass

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

    #Find groups for given user and the find notices for that groups
    #Use paginate_objects method from common.utils to get the list of objects
    pass

def get_notices(creator, return_all=False, page_no=1, paginate=True):
    """
    Returns notices to edit
    Params:
        creator: User object
        return_all: weather to apply creator filter or not
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """
    pass

def publish_notice(notice):
    """
    Publishes the given notice
    Params:
        notice: Notice object
        send_notification: Boolean. Weather to send email/sms notification
    """
    pass

def get_notice_obj(notice_id):
    """
    Returns the notice object with given id
    Params:
        notice_id : Notice id
    """
    pass
