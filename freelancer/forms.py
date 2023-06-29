from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *


class ApplyForm(forms.Form):
    job = forms.ChoiceField(choices=[('A', 'Freelancer'), ('B', 'Employer')], widget=forms.RadioSelect(attrs={
        "class": "",
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                 "mb-3 leading-tight focus:outline-none focus:bg-gray-100 text-center px-4",
        'placeholder': _('Description')
    }))

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                     'px-4 mb-3 focus:outline-none focus:bg-gray-300 conditional-field',
        })
    )

    def conditional_fields(self):
        if self['job'].value() == 'A':
            return ['skill']
        else:
            return []

    def get_visible_fields(self):
        visible_fields = list(self.fields.keys())
        conditional_fields = self.conditional_fields()
        for field_name in conditional_fields:
            if field_name in visible_fields:
                visible_fields.remove(field_name)
        return visible_fields


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'price', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-gray-100 text-center px-4",
                'placeholder': _('Title')
            }),
            'description': forms.Textarea(attrs={
                'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-gray-100 text-center px-4",
                'placeholder': _('Description')
            }),
            'price': forms.NumberInput(attrs={
                'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-gray-100 text-center px-4",
                'placeholder': _('Price')
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 focus:outline-none focus:bg-gray-300',
            }),
        }
