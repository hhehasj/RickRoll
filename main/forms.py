from django import forms
from django.forms import ModelForm
from .models import Player, Random_Letter


class playerform(ModelForm):
    class Meta:
        model = Player
        fields = ("name",)
        labels = {
            "name": "",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}, )
        }


class answersform(ModelForm):
    class Meta:
        model = Random_Letter
        fields = ("letter", )
        labels = {
            "letter": ""
        }

        widgets = {
            "letter": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a letter"})

        }