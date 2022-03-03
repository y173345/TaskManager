from django import forms
from .models import Task


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "issue_date", "deadline", ]
