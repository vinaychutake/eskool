"""
"""

from django import forms

class CustomCharField(forms.CharField):
    """
    """

    def __init__(self, *args, **kwargs):
    	self.has_group_addon = kwargs.pop('has_group_addon', False)
    	if self.has_group_addon:
    		self.glyphicon_class = kwargs.pop('glyphicon_class') 

		super(CustomCharField, self).__init__(*args, **kwargs)

class CustomDateField(forms.DateField):
    """
    """

    def __init__(self, *args, **kwargs):

    	self.has_group_addon = kwargs.pop('has_group_addon', False)
    	if self.has_group_addon:
    		self.glyphicon_class = kwargs.pop('glyphicon_class') 

		super(CustomDateField, self).__init__(*args, **kwargs)

class CustomModelChoiceField(forms.ModelChoiceField):
	"""
	"""

	def __init__(self, *args, **kwargs):

		self.has_group_addon = kwargs.pop('has_group_addon', False)
		if self.has_group_addon:
			self.glyphicon_class = kwargs.pop('glyphicon_class') 

		super(CustomModelChoiceField, self).__init__(*args, **kwargs)

class CustomChoiceField(forms.ChoiceField):
	"""
	"""

	def __init__(self, *args, **kwargs):

		self.has_group_addon = kwargs.pop('has_group_addon', False)
		if self.has_group_addon:
			self.glyphicon_class = kwargs.pop('glyphicon_class') 

		super(CustomChoiceField, self).__init__(*args, **kwargs)
