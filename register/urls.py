from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('equip_add/', views.EqAdd.as_view(), name='equip_add'),
    path('equip_update/<int:pk>', views.EqUpdate.as_view(), name='equip_update'),
    path('equip_delete/<int:pk>', views.EqDelete.as_view(), name='equip_delete'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('user_add/', views.UserAdd.as_view(), name='user_add'),
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    path('user_delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),

]