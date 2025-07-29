from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.views import PasswordChangeView

from user.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Введіть Логін', widget=forms.TextInput())
    password1 = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Підтвердіть пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старий пароль', widget=forms.TextInput())
    new_password1 = forms.CharField(label='Новий пароль', widget=forms.TextInput())
    new_password2 = forms.CharField(label='Підтвердження паролю', widget=forms.TextInput())

    class Meta:
        model = User


