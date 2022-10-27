from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Notes, User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AddNoteForm(forms.ModelForm):

    user = User.username
    category = Category.user

    class Meta:
        model = Notes
        fields = ['title', 'image', 'body', 'category', 'user']


class EditNoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['title', 'image', 'body', 'category', 'user']


class AddCategoryForm(forms.ModelForm):

    user = User.username

    class Meta:
        model = Category
        fields = ['name', 'user']
