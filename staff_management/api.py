"""

"""

from staff_management.models import Staff, Teacher

from common.utils import paginate_objects

def get_non_teaching_staff(page_no=1, paginate=True, records_per_page=10):
    """
    Returns list of non teaching staff
    Params:
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """

    staff = Staff.objects.filter(user__is_active=True)
    count = len(staff)
    if paginate:
        staff = paginate_objects(staff, records_per_page, page_no=page_no)
    return {'staff': staff, 'count': count, 'returned_count': len(staff)}

def get_teachers(page_no=1, paginate=True, records_per_page=10):
    """
    Returns list of teachers
    Params:
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """

    teachers = Teacher.objects.filter(staff__user__is_active=True)
    count = len(teachers)
    if paginate:
        teachers = paginate_objects(teachers, records_per_page, page_no=page_no)
    return {'teachers': teachers, 'count': count, 'returned_count': len(teachers)}
