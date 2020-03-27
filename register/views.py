from django.shortcuts import render
from .models import User, Equipment
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

 

class EqDetail(DetailView):
    template_name = 'register/eq_detail.html'
    model = Equipment

class EqUpdate(UpdateView):
    template_name = 'register/equip_update.html'
    model = Equipment
    fields = ['name', 'category',  'price', 'comment']

    def get_success_url(self):
 
        return reverse('staff:equip_list')

class AddEquipment(CreateView):
    template_name = 'register/equip_add.html'
    model = Equipment
    fields = ['name', 'category',  'price', 'comment']

    def get_success_url(self):
        return reverse('register:equip_add')