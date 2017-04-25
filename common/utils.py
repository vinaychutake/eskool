"""
Utility functions
"""
import re

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_objects(objects, objects_per_page, page_no=None):
    """
    Paginates the given list of objects according to page count and page number
    """

    paginator = Paginator(objects, objects_per_page)

    try:
        page_objects = paginator.page(page_no)
    except PageNotAnInteger:
        page_objects = paginator.page(1)
    except EmptyPage:
        page_objects = paginator.page(paginator.num_pages)

    return page_objects


def check_email_validity(email):
    email_regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    match = re.match(email_regex, email)
    if match == None:
        return False
    else:
        return True