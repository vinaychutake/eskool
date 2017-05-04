from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.forms.widgets import SelectMultiple

class AcademicsForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=48,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 48 characters are allowed'))