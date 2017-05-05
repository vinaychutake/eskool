from common.utils import paginate_objects
from academics_management.models import Standard
import pdb
def create_standard(template, year, status):
    """
    Creates new standard
    Params:
        name: Subjec name
        status: Active or inactive
        code: Standard code
    """
    standard = Standard(name='%s-(%s)'%(template,year),
                    academic_year=year,
                    status=status,
                    standard_template=template)
    standard.full_clean()
    standard.save()
    subjects=template.subjects
    return standard.id

def get_standards(page_no=1, paginate=True, records_per_page=10):
    """
    Returns standards for given user
    Params:
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    Returns:
        Standards in json format
    """
    standards = Standard.objects.exclude(status='D')

    return paginate_standards(paginate, standards, records_per_page, page_no)


def paginate_standards(paginate, standards, records_per_page, page_no):
    """
    """
    count = len(standards)
    if paginate:
        standards = paginate_objects(standards, records_per_page, page_no) 
    return {'standards': standards, 'count': count, 'returned_count': len(standards)}


def delete_standard(standard_id):
    """
    Returns the standard object with given id
    Params:
        standard_id : Standard id
    """
    standard = get_standard_obj(standard_id)
    standard.delete()
        

def get_standard_obj(standard_id):
    """
    Returns the standard object with given id
    Params:
        standard_id : Standard id
    """
    standard = Standard.objects.get(id=standard_id)
    return standard        

  