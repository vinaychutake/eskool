"""

"""

from staff_management.models import Staff, Teacher

from common.utils import paginate_objects

from auth_management.models import User
from tenant_management.models import Address, ContactNumber

def get_staff(page_no=1, paginate=True, records_per_page=10):
    """
    Returns list of non teaching staff
    Params:
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """

    staff = Staff.objects.filter(user__is_active=True).exclude(staff_type__code='TC')
    if paginate:
        staff = paginate_objects(staff, records_per_page, page_no=page_no)
    return staff

def get_teachers(page_no=1, paginate=True, records_per_page=10):
    """
    Returns list of teachers
    Params:
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """

    teachers = Teacher.objects.filter(staff__user__is_active=True)
    if paginate:
        teachers = paginate_objects(teachers, records_per_page, page_no=page_no)
    return teachers

def create_user(username, first_name, middle_name, last_name, date_of_birth,
                email, profile_pic, gender):
    """
    """

    return User.objects.create_user(username=username, first_name=first_name,
                                    middle_name=middle_name, last_name=last_name,
                                    birth_date=date_of_birth, email=email,
                                    profile_pic=profile_pic, gender=gender)

def add_user_address(user, address1, address2, address3, city):
    """
    """

    address = Address.objects.create(address1=address1, address2=address2,
                                     address3=address3, city=city)
    user.addresses.add(address)

def add_user_contactnumber(user, contact_number):
    """
    """

    contact_num, is_created = ContactNumber.objects.get_or_create(contact_number=contact_number)
    user.contact_numbers.add(contact_num)

def create_staff(user, staff_type, joining_date, reporting_to):
    """
    """

    Staff.objects.create(staff_type=staff_type, joining_date=joining_date, user=user,
                         reporting_to=reporting_to.user)
