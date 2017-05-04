from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import StatusMixin

from staff_management.models import Teacher 

class AcademicYear(StatusMixin):
    """
    Class representing an academis year e.g. 2015-16
    """

    name = models.CharField(_('Name'), max_length=12, unique=True, null=False,
                            blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acm_academic_year'

class Subject(StatusMixin):
    """
    Class representing a subject e.g. Mathematics, History
    """

    name = models.CharField(_('Name'), max_length=80, unique=True, null=False,
                            blank=False)

    teachers = models.ManyToManyField(Teacher, related_name='subjects')
    creted_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    code = models.CharField(max_length=16, unique=True, null=False, blank=False)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acm_subject'

class StandardTemplate(StatusMixin):
    """
    Class representing a standard template e.g. 5th
    """

    name = models.CharField(_('Name'), max_length=48, unique=True, null=False,
                            blank=False)

    code = models.CharField(_('Code'), max_length=16, unique=True, null=False,
                            blank=False)

    is_frozen = models.BooleanField(default=False, null=False, blank=False)

    subjects = models.ManyToManyField(Subject, related_name='standard_templates')

    def __str__(self):
        return self.name 

    class Meta:
        db_table = 'acm_standard_template'

class Standard(StatusMixin):
    """
    Class representing an actual standart. e.g. 5th (2015-16)
    """

    name = models.CharField(_('Name'), max_length=80, unique=True, null=False,
                            blank=False)

    standard_template = models.ForeignKey(StandardTemplate, related_name='standards')

    academic_year = models.ForeignKey(AcademicYear, related_name='standards')

    subjects = models.ManyToManyField(Subject, related_name='standerds')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acm_standard'

class Division(StatusMixin):
    """
    Class representing an division e.g. 5th (2015-16)/A, 5th (2015-16)/B
    """

    name = models.CharField(_('Name'), max_length=80, unique=True, null=False,
                            blank=False)

    standard = models.ForeignKey(Standard, related_name='divisions')

    subjects = models.ManyToManyField(Subject, through='DivisionSubjectMap')

    class_teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acm_division'

class DivisionSubjectMap(models.Model):
    """
    Class representing mapping between division and subject
    """

    division = models.ForeignKey(Division)

    subject = models.ForeignKey(Subject)

    teachers = models.ManyToManyField(Teacher)

    class Meta:
        db_table = 'acm_division_subject_map'