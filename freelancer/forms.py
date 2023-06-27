from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *


class ApplyForm(forms.Form):
    pass  # Class to apply to be a freelancer or employer


# TODO: Create an apply form


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'price', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-white text-center px-4",
                'placeholder': _('Title')
            }),
            'description': forms.Textarea(attrs={
                'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-white text-center px-4",
                'placeholder': _('Description')
            }),
            'price': forms.NumberInput(attrs={
                'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-white text-center px-4",
                'placeholder': _('Price')
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 focus:outline-none focus:bg-gray-300',
            }),
        }
