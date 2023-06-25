from django import forms

from .models import *


class ApplyForm(forms.Form):
    pass  # Class to apply to be a freelancer or employer


# TODO: Create an apply form


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
# TODO: Customize the form
