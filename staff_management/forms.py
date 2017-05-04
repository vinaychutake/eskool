from django.utils.translation import ugettext_lazy as _
from django import forms

from common.choices import GENDER_CHOICES
from tenant_management.models import State, City
from staff_management.models import StaffType, Staff
from common import fields as custom_fields

class StaffForm(forms.Form):
    """
    """

    staff_type = custom_fields.CustomModelChoiceField(queryset=StaffType.objects.exclude(code='TA'),
                                                      required=True, help_text=_('Select type of staff you want to add.'),
                                                      widget=forms.Select(attrs={'class':'form-control'}),
                                                      has_group_addon=True,
                                                      glyphicon_class='chevron-down')

    username = custom_fields.CustomCharField(max_length=48,
                                             required=True,
                                             widget=forms.TextInput(attrs={'class':'form-control'}),
                                             help_text=_('Must be unique.   Maximum 48 characters are allowed'),
                                             has_group_addon=True,
                                             glyphicon_class='user')

    first_name = forms.CharField(max_length=48, required=True,
                                 widget=forms.TextInput(attrs={'class':'form-control'}),
                                 help_text=_('Maximum 48 characters are allowed.'))

    middle_name = forms.CharField(max_length=48, required=False,
                                  widget=forms.TextInput(attrs={'class':'form-control'}),  
                                  help_text=_('Maximum 48 characters are allowed.'))

    last_name = forms.CharField(max_length=48, required=True,
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                help_text=_('Maximum 48 characters are allowed.'))

    date_of_birth = custom_fields.CustomDateField(required=True,
                                                  widget=forms.TextInput(attrs={'class':'form-control datepicker'}),
                                                  help_text=_('Select date of birth of user.'),
                                                  has_group_addon=True,
                                                  glyphicon_class='calendar')

    joining_date = custom_fields.CustomDateField(required=True,
                                                 widget=forms.TextInput(attrs={'class':'form-control datepicker'}),
                                                 help_text=_('Select joining date of user.'),
                                                 has_group_addon=True,
                                                 glyphicon_class='calendar')

    email = forms.EmailField(required=False,
                             help_text=_('Enter valid email address, It must be unique'),
                             widget=forms.TextInput(attrs={'class':'form-control'}))

    profile_pic = forms.ImageField(required=False, help_text=_('Upload picture of user.'),
                                   widget=forms.TextInput(attrs={'type': 'file',
                                                                 'id': 'profile-pic'
                                                                }))

    gender = custom_fields.CustomChoiceField(choices=GENDER_CHOICES,
                                             required=True,
                                             widget=forms.Select(attrs={'class':'form-control'}),
                                             has_group_addon=True,
                                             glyphicon_class='chevron-down',
                                             help_text=_('Select gender of user'))

    contact_num = custom_fields.CustomCharField(required=True,
                                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                                has_group_addon=True,
                                                glyphicon_class='phone-alt',
                                                help_text=_('Enter a valid contact number'))

    reporting_to = custom_fields.CustomModelChoiceField(queryset=Staff.objects.all(), required=False,
                                                        widget=forms.Select(attrs={'class':'form-control'}),
                                                        has_group_addon=True,
                                                        glyphicon_class='chevron-down',
                                                        help_text=_('Select mentor of this user'))

    address1 = forms.CharField(max_length=20, required=True,
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               help_text=_('e.g. Plot no-8/9, Apate Nagar'))

    address2 = forms.CharField(max_length=20, required=False,
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               help_text=_('e.g. Near New vashi naka'))

    address3 = forms.CharField(max_length=20, required=False,
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               help_text=_('e.g. Kolhapur'))

    state = custom_fields.CustomModelChoiceField(queryset=State.objects.all(), required=True,
                                                 widget=forms.Select(attrs={'class':'form-control'}),
                                                 has_group_addon=True,
                                                 glyphicon_class='chevron-down',
                                                 help_text=_('Select state'))

    city = custom_fields.CustomModelChoiceField(queryset=City.objects.all(), required=True,
                                                widget=forms.Select(attrs={'class':'form-control'}),
                                                has_group_addon=True,
                                                glyphicon_class='chevron-down',
                                                help_text=_('Select city'))
