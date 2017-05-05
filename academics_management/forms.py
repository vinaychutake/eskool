from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import CheckboxSelectMultiple

from common import choices
from academics_management.models import Subject,StandardTemplate,AcademicYear

class AcademicYearForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=12,
                           required=True,
                           widget=forms.TextInput(attrs={'class':'form-control'}),
                           help_text=_('Maximum 12 characters are allowed'))
 
    status = forms.ChoiceField(choices=choices.STATUS_CHOICES, required=True)

class SubjectForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=80,
                           required=True,
                           widget=forms.TextInput(attrs={'class':'form-control'}),
                           help_text=_('Maximum 80 characters are allowed'))
    
    code = forms.CharField(max_length=16,
                           required=True,
                           widget=forms.TextInput(attrs={'class':'form-control'}),
                           help_text=_('Maximum 16 characters are allowed'))

    status = forms.ChoiceField(choices=choices.STATUS_CHOICES,required=True)

class STDTemplateForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=80,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 80 characters are allowed'))
    
    code = forms.CharField(max_length=16,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 16 characters are allowed'))

    subjects = forms.ModelMultipleChoiceField(Subject.objects.exclude(status='D'),
                                              required=True,
                                              widget=CheckboxSelectMultiple(),
                                              help_text=_('Select subjects to add in this template.'))


class StandardForm(forms.Form):
    """
    """    
    template = forms.ModelChoiceField(StandardTemplate.objects.exclude(status='D'),
                                  required=True,
                                  help_text=_('Select template to add in this Standard.'))

 
    year = forms.ModelChoiceField(AcademicYear.objects.exclude(status='D'),
                                  required=True,
                                  help_text=_('Select year to add in this Standard.'))


    status = forms.ChoiceField(choices=choices.STATUS_CHOICES,required=True)