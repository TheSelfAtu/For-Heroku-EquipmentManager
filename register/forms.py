from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

# 一般ユーザー用　サインアップ
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'department',)

# スタッフ用　サインアップ
class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'department', 'is_staff',)