from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index')
]
