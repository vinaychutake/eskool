from academics_management.models import AcademicYear
from common.utils import paginate_objects

def create_academics_year(name, status):
    """
    """
    year = AcademicYear(name=name, status=status)
    year.full_clean()
    year.save()
    return year.id

def get_academic_year_obj(year_id):
    """
    """

    return AcademicYear.objects.get(id=year_id)

def get_academic_years(records_per_page=10, page_no=1, paginate=True):
    """
    """

    academic_years = AcademicYear.objects.exclude(status='D')
    count = len(academic_years)
    if paginate:
        academic_years = paginate_objects(academic_years, records_per_page, page_no)
    return {'years': academic_years, 'count': count, 'returned_count': len(academic_years)}

def delete_year(year_id):
    """
    """
    year = get_academic_year_obj(year_id)
    year.delete()

def update_year(year_id, year_name, status):

    year = get_academic_year_obj(year_id)
    year.name = year_name
    year.status = status
    year.full_clean()
    year.save()

