

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from user.models import User
from user.static.user.forms import RegisterUserForm, LoginUserForm, ChangePasswordForm

menu = [{'title': "Проєкти",'url_name': 'project'}, {'title': "Про автора", "url_name": 'about'}]


# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    template_name = 'projects/register/register.html'
    extra_context = {'title': 'Реєстрація'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context1 = super().get_context_data(**kwargs)

        context1['menu'] = menu
        context1['addurl'] = "addpage"

        return context1

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'projects/login/login.html'
    extra_context = {"title": "Авторизація"}

    def get_context_data(self, *,object_list=None ,**kwargs):
        context1 = super().get_context_data(**kwargs)
        context1['menu'] = menu
        context1['addurl'] = "addpage"
        return context1


class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'projects/changepass/changepass.html'
    success_url = 'projects/changepass/success.html'
    extra_context = {'title': 'Зміна пароля'}

    def get_context_data(self, *,object_list=None ,**kwargs):
        context1 = super().get_context_data(**kwargs)
        context1['menu'] = menu
        context1['addurl'] = "addpage"
        return context1

def logout1(request):
    logout(request)
    return redirect('login')

