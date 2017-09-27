from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Messages, encMessages
from django.core.validators import ValidationError
from django.core import validators


class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cnfpassword = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']



class usrPost(forms.ModelForm):
    #file = forms.FileField(widget=forms.FileInput(attrs={'onchange':'encryptfile()'}))
    class Meta:
        model = Post
        fields = [
            "postname",
            "Content",
            "file",

        ]

class usrMessage(forms.ModelForm):
    class Meta:
        model = Messages
        fields = [
            "title",
            "message",

        ]

class usrEncMessage(forms.ModelForm):
    class Meta:
        model = encMessages
        fields = [
            "title",
            "encrypted_message",
        ]