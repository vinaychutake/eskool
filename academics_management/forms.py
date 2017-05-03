from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.forms.widgets import SelectMultiple
from common import choices
 
class SubjectForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=80,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 80 characters are allowed'))
    status = forms.ChoiceField(choices=choices.STATUS_CHOICES,required=True)

    code = forms.CharField(max_length=16,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 16 characters are allowed'))


