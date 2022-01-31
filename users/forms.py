from dataclasses import field
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User

GENDER_CHOICES=(
    ("Erkak","Erkak"),
    ("Ayol","Ayol")
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={"placeholder":"email", "class":"form-control"}))
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username","class":"form-control" }))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password","class":"form-control"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"re-password","class":"form-control"}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"last name","class":"form-control"}))
    phone = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"phone","class":"form-control"}))

    class Meta:
        model = User
        fields = ("username", "last_name","email", "phone", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username","class":"form-control" }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password","class":"form-control"}))

    class Meta:
        model=User
        fields=("username","password")

