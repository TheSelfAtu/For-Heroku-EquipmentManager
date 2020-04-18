from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import User, Equipment
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from .forms import UserAddForm, SignupForm

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

# ユーザー作成
class SignupView(CreateView):
    form_class = SignupForm
    template_name = "register/user_signup.html" 
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('accounts:login') # リダイレクト

# スタッフ用ユーザー追加　is_staffをTrueにできる。
class UserAdd(CreateView):
    form_class = UserAddForm
    template_name = 'register/user_add.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('staff:staff_page')
 
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