from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.HomeView.as_view(), name='user_page'),
    path('equip_list', views.EquipListView.as_view(), name='equip_list'),
   
]