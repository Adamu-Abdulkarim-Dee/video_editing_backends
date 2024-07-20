from django.urls import path
from  . import views

urlpatterns = [
    #The url endpoint that you are goint to use to upload video 
    path('PostFileView', views.PostFileView.as_view(), name='PostFileView')
]