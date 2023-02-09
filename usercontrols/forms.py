from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comments


class UserRedirecterForms(UserCreationForm):

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите свой логин', 'width': '100%'}))

    password1 = forms.CharField(label='Введите пароль', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите свой пароль'}))

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'повторите пароль'}))
    email = forms.EmailField(label='Введите ваш EMAIL', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите свой логин', 'width': '100%'}))

    password = forms.CharField(label='Введите пароль', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите свой пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)