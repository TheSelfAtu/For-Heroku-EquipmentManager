from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('', views.HomeView.as_view(), name='staff_page'),
    path('equip_list', views.EquipListView.as_view(), name='equip_list'),
    path('loan/<int:pk>/', views.loan, name='loan'),
    path('return_eq/<int:pk>/', views.return_eq, name='return_eq'),
    
]