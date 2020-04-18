from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import LoginForm

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

class MyLogoutView(LogoutView):
    template_name = "accounts/logout.html"

class RedirectView(TemplateView):
    template_name = 'user/home.html'


