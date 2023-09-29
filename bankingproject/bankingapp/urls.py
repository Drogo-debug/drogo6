from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('',views.home,name='home'),
    path('login/',views.loging, name='login'),
    path('register/',views.register,name='register'),
    path('back/',views.back,name='back')
    ]