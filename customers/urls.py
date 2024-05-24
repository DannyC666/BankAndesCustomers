# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('cliente_registrado/', views.cliente_registrado, name='cliente_registrado'),
    path('ver_clientes/', views.ver_clientes, name='ver_clientes'),
]
