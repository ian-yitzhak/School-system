from django.urls import path 

from . import views

urlpatterns = [

    path('', views.home , name ="iano-home" ),
    path('/contact', views.contact , name = "iano-contact"),
    
   


]