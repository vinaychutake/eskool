from django.utils.translation import ugettext_lazy as _
from django import forms

from common.choices import GENDER_CHOICES
from tenant_management.models import State, City
from staff_management.models import StaffType, Staff

class StaffForm(forms.Form):
    """
    """

    staff_type = forms.ModelChoiceField(queryset=StaffType.objects.all(), required=True, help_text=_('role'))

    username = forms.CharField(max_length=48,
                               required=True,
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               help_text=_('Username must be unique. Maximum 48 characters are allowed'))

    first_name = forms.CharField(max_length=48, required=True,
                                 widget=forms.TextInput(attrs={'class':'form-control'}),
                                 help_text=_('Maximum 48 characters are allowed.'))

    middle_name = forms.CharField(max_length=48, required=True,
                                  widget=forms.TextInput(attrs={'class':'form-control'}),  
                                  help_text=_('Maximum 48 characters are allowed.'))

    last_name = forms.CharField(max_length=48, required=True,
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                help_text=_('Help text'))

    date_of_birth = forms.DateField(required=True,
                                    widget=forms.TextInput(attrs={'class':'form-control'}),
                                    help_text=_('Help text'))

    joining_date = forms.DateField(required=True,
                                   widget=forms.TextInput(attrs={'class':'form-control'}),
                                   help_text=_('Help text'))

    email = forms.EmailField(required=False,
                             help_text=_('Help text'),
                             widget=forms.TextInput(attrs={'class':'form-control'}))

    profile_pic = forms.ImageField(required=False, help_text=_('Help text'),
                                   widget=forms.TextInput(attrs={'class':'file',
                                                                  'data-preview-file-type': 'any',
                                                                  'type': 'file'
                                                                  }))

    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               required=True,
                               help_text=_('Help text'))

    contact_num = forms.CharField(required=True, help_text=_('contact number'))

    reporting_to = forms.ModelChoiceField(queryset=Staff.objects.all(), required=True, help_text=_('reporting to'))

    state = forms.ModelChoiceField(queryset=State.objects.all(), required=True, help_text=_('contact number'))

    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True, help_text=_('contact number'))


    address1 = forms.CharField(max_length=20, required=True, help_text=_('address1'))

    address2 = forms.CharField(max_length=20, required=False, help_text=_('contact number'))

    address3 = forms.CharField(max_length=20, required=False, help_text=_('contact number'))
