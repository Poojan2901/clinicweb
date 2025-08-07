from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_clinic, name='register_clinic'),
    path('login/', views.login_clinic, name='login_clinic'),
    path('logout/', views.logout_clinic, name='logout_clinic'),
]
