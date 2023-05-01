from django.urls import path
from oficinaApp import views

urlpatterns = [ 
    path('fichas', views.fichas, name='Fichas'),
    path('fichas/<ficha>', views.ficha, name='Ficha')
               ]