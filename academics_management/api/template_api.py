from common.utils import paginate_objects
from academics_management.models import StandardTemplate


def get_std_templates(return_all=False, page_no=1, paginate=True, records_per_page=10):
    """
    Returns notices to edit
    Params:
        creator: User object
        return_all: weather to apply creator filter or not
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    """
    templates = StandardTemplate.objects.exclude(status='D')
    count = len(templates)
    if paginate:
        templates = paginate_objects(templates, records_per_page, page_no) 
    return {'std_templates': templates, 'count': count, 'returned_count': len(templates)}

def create_std_template(name, code, subjects):
    """
    Creates new standard template
    Params:
        name: Name of template
        code : code of template
        subjects: List of subject names
    """

    std_template = StandardTemplate(name=name,
                    code=code)
    std_template.full_clean()
    std_template.save()
    std_template.subjects = subjects

def update_std_template(std_template_id, name, code, subjects):
    """
    Update existing standard template
    Params:
        std_template_id: std template id which is going to be updated
        name: Name of template
        code : code of template
        subjects: List of subject names
    """

    std_template = get_std_template_obj(std_template_id)
    std_template.subjects = subjects
    std_template.name = name
    std_template.code = code
    std_template.full_clean()
    std_template.save()

def get_std_template_obj(std_template_id):
    """
    Returns the standard template object with given id
    Params:
        std_template_id : Standard Template id
    """
    std_template = StandardTemplate.objects.get(id=std_template_id)
    return std_template

def delete_std_template(std_template_id):
    """
    Returns the template object with given id
    Params:
        std_template_id : Standard Template id
    """
    std_template = get_std_template_obj(std_template_id)
    std_template.delete()
