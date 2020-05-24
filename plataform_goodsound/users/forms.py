from django import forms
from django.forms import ModelForm

from .models import Users


class UserModelForm(forms.ModelForm):
    avatar = forms.ImageField()
    class Meta:
        model = Users
        fields = "__all__"
        widgets = {
            'avatar': forms.FileInput(),
        }


