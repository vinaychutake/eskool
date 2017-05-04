from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.forms.widgets import SelectMultiple

from academics_management.models import Subject

class STDTemplateForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=48,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 48 characters are allowed'))

    code = forms.CharField(max_length=16,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 16 characters are allowed'))

    subjects = forms.ModelMultipleChoiceField(Subject.objects.all(), required=True,
                                        widget=SelectMultiple(attrs={'class': 'form-control select',
                                                                     'data-live-search': "true"}),
                                        help_text=_('Select subjects to add in this template.'))


