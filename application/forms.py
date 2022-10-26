from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Notes, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateNote(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'image', 'body']


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']