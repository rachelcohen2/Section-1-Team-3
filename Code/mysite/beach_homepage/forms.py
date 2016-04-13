#files.py
import re
from django import forms
from polls.models import property
from django.utils.translation import ugettext_lazy as _

class PropRegistrationForm(forms.Form):

    Name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Property Name"))
    Price = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Price"))
    Location = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Location"))
    #Image = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Image"))
    Owner = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Owner"))
    Description = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=256)), label=_("Description"))

    def clean_username(self):
        try:
            prop = property.objects.get(Name__iexact=self.cleaned_data['Name'])
        except prop.DoesNotExist:
            return self.cleaned_data['Name']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    #def clean(self):
    #    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
 #               raise forms.ValidationError(_("The two password fields did not match."))
  #      return self.cleaned_data
