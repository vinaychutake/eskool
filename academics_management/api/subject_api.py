from common.utils import paginate_objects
from academics_management.models import Subject

def get_subjects(page_no=1, paginate=True, records_per_page=10):
    """
    Returns subjects for given user
    Params:
        page_no: page_no
        paginate: If False return all objects, else return objects on given page
    Returns:
        Subjects in json format
    """
    subjects = Subject.objects.exclude(status='D')

    return paginate_subjects(paginate, subjects, records_per_page, page_no)


def paginate_subjects(paginate, subjects, records_per_page, page_no):
    """
    """
    count = len(subjects)
    if paginate:
        subjects = paginate_objects(subjects, records_per_page, page_no) 
    return {'subjects': subjects, 'count': count, 'returned_count': len(subjects)}


def delete_subject(subject_id):
    """
    Returns the subject object with given id
    Params:
        subject_id : Subject id
    """
    subject = get_subject_obj(subject_id)
    subject.delete()
        

def get_subject_obj(subject_id):
    """
    Returns the subject object with given id
    Params:
        subject_id : Subject id
    """
    subject = Subject.objects.get(id=subject_id)
    return subject        

def update_subject(subject_id, name, status, code):
    """
    Update subject
    Params:
        subject_id: subject id which is going to be updated
        name: Name of subject
        status: Subject status
        code: Subject code
    """

    subject = get_subject_obj(subject_id)
    subject.name = name
    subject.status = status
    subject.code = code
    subject.clean()
    subject.save()    