from django.utils.translation import ugettext_lazy as _
from django import forms

class UserForm(forms.Form):
    """
    """

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

    email = forms.EmailField(required=False,
                             help_text=_('Help text'),
                             widget=forms.TextInput(attrs={'class':'form-control'}))

    profile_pic = forms.ImageField(required=False, help_text=_('Help text'),
                                   widget=forms.TextInput(attrs={'class':'file',
                                                                  'data-preview-file-type': 'any',
                                                                  'type': 'file'
                                                                  }))

    gender = forms.CharField(max_length=48, required=True, help_text=_('Help text'))

    contact_num = forms.CharField(max_length=20, required=True, help_text=_('contact number'))

    state = forms.CharField(max_length=20, required=True, help_text=_('contact number'))

    city = forms.CharField(max_length=20, required=True, help_text=_('contact number'))

    address1 = forms.CharField(max_length=20, required=True, help_text=_('contact number'))

    address2 = forms.CharField(max_length=20, required=True, help_text=_('contact number'))

    address3 = forms.CharField(max_length=20, required=True, help_text=_('contact number'))

    subjects = forms.CharField(max_length=20, required=True, help_text=_('contact number'))
