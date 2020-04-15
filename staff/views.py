from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from register.models import User, Equipment
from .forms import LoanForm
from datetime import date, timedelta 

class HomeView(generic.TemplateView):
    template_name = 'staff/home.html'


class EquipListView(generic.TemplateView):
    template_name = 'staff/equip_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equip_list'] = Equipment.objects.all()
        return context

def loan(request, pk):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=form.cleaned_data.get('userID')) 
            equip = Equipment.objects.get(id=pk)
            equip.belong_to = user
            equip.return_date = timedelta(form.cleaned_data.get('loan_day')) + date.today()
            equip.save()
            return redirect('staff:equip_list')
        else:
            return render(request, 'staff/loan.html', {'form':form})

    equipment = Equipment.objects.get(pk=pk)
    context = {
        'equipment':equipment,
        'form':LoanForm()
    }
    return render(request, 'staff/loan.html', context)

def return_eq(request, pk):
    equip = Equipment.objects.get(id=pk)
    equip.belong_to = None
    equip.return_date = None
    return_date = date.today()
    equip.save()
    return redirect('staff:equip_list')


class UserListView(generic.TemplateView):
    template_name = 'staff/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context
