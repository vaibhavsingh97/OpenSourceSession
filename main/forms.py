from django import forms

from main.models import StudentRegisterationForm


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = StudentRegisterationForm
        fields = ('name', 'email', 'branch', 'year', 'github_url')