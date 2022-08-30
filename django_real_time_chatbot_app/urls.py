from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'), #dynamic url
    path('checkview', views.checkview, name='checkview'), #it collects & checks the data submitted by the html form from the user -first
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]

