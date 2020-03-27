from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.RedirectView.as_view(), name='show_home'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
]