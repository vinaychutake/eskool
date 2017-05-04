from academics_management.models import AcademicYear
from common.utils import paginate_objects

def create_academics_year(name):
	year = AcademicYear(name=name)
	year.clean()
	year.save()

def get_all_years():
	academic_years = AcademicYear.objects.all()
	return paginate_years(academic_years)

def delete_year(year_id):
    """

    """
    year = AcademicYear.objects.get(id=year_id)
    year.delete()

def update_year(year_id, year_name, year_status):

    year = AcademicYear.objects.get(id=year_id)
    year.name = year_name
    #year.status = year_status
    year.save()

def paginate_years(years, records_per_page=10, page_no=1, paginate=True):
    """
    """
    count = len(years)
    if paginate:
        years = paginate_objects(years, records_per_page, page_no)
    return {'years': years, 'count': count, 'returned_count': len(years)}
