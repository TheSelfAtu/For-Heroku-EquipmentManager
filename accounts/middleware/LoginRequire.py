import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class LoginRequiredMiddleware(MiddlewareMixin):
    # サインアップ以外の機能のログインを必須にする
    def process_response(self, request, response):
        # サインアップは許可
        if request.path == '/register/signup/':
            return response
        # 他の機能はログイン必須
        if request.path != '/accounts/login/' and not request.user.is_authenticated:         
            return HttpResponseRedirect('/accounts/login/')
        return response

class StaffRequiredMiddleware(MiddlewareMixin):
    # 一般ユーザーをスタッフページにアクセスさせない
    def process_response(self, request, response):
        staff_path = r'^/staff/'
        if re.match(staff_path, request.path) and not request.user.is_staff:
            return HttpResponseRedirect('/user/')
        return response