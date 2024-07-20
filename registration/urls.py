from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('UserRegistrationView/', views.UserRegistrationView.as_view(), 
    name='UserRegistrationView'), #This is the url endpoint for user registration page

    path('UserLoginView/', views.UserLoginView.as_view(), 
    name='UserLoginView'), #This is the url endpoint for Login page
]