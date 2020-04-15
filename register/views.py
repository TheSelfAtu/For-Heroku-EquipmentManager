from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import User, Equipment
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# 備品追加
class EqAdd(CreateView):
    template_name = 'register/equip_add.html'
    model = Equipment
    fields = ['name', 'category',  'price', 'comment']

    def get_success_url(self):
        return reverse('register:equip_add')

# 備品情報更新
class EqUpdate(UpdateView):
    template_name = 'register/equip_update.html'
    model = Equipment
    fields = ['name', 'category',  'price', 'comment']

    def get_success_url(self):
 
        return reverse('staff:equip_list')

# 備品詳細
class EqDetail(DetailView):
    template_name = 'register/eq_detail.html'
    model = Equipment

# 備品削除
class EqDelete(DeleteView):
    template_name = 'register/equipment_confirm_delete.html'
    model = Equipment
    success_url = reverse_lazy('staff:equip_list')

#
# ユーザー追加 関数ベースなのはパスワードをハッシュ化するため
def UserAdd(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            print(raw_password)
            user.set_password(raw_password)
            user.save()
            return redirect("staff:staff_page")
    else:
        form = UserCreationForm()
    return render(request, 'register/user_add.html', {"form":form})

# ユーザー情報更新
class UserUpdate(UpdateView):
    template_name = 'register/user_update.html'
    model = User
    fields = ['first_name', 'last_name',  'email', 'department', ]

    def get_success_url(self):
        return reverse('staff:user_list')

# ユーザー削除
class UserDelete(DeleteView):
    template_name = 'register/user_confirm_delete.html'
    model = User
    success_url = reverse_lazy('staff:user_list')