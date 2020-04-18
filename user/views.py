from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from register.models import User, Equipment, Loan_log, Return_log
from datetime import date, timedelta 


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'user/home.html'


class EquipListView(generic.TemplateView):
    template_name = 'user/equip_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equip_list'] = Equipment.objects.all()
        return context
