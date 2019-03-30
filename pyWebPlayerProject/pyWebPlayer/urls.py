from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getFiles/', views.getFiles, name='getFiles'),
    path('updateDBRequest/', views.updateDBRequest, name='updateDBRequest'),
]
