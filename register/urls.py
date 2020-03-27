from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('equip_add', views.AddEquipment.as_view(), name='equip_add'),
    path('equip_update/<int:pk>', views.EqUpdate.as_view(), name='equip_update'),
    
]