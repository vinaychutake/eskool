from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.forms.widgets import SelectMultiple

class NoticeForm(forms.Form):
    """
    """

    title = forms.CharField(max_length=48,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            help_text=_('Maximum 48 characters are allowed'))

    to = forms.ModelMultipleChoiceField(Group.objects.all(), required=True,
                                        widget=SelectMultiple(attrs={'class': 'form-control select',
                                                                     'data-live-search': "true"}),
                                        help_text=_('Select groups who can see this notice.'))

    notice = forms.CharField(widget=forms.Textarea(attrs={'class':'summernote'}))


