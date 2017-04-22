"""
Utility functions
"""

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