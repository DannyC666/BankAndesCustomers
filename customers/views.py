# views.py

from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            nuevo_cliente = Cliente(
                    DNI=data['dni'],
                    nombre=data['nombre'],
                    email=data['email'],
                    profesion=data['profesion'],
                    actividad_economica=data['actividad_economica'],
                    empresa=data['empresa'],
                    ingresos=data['ingresos'],
                    deudas=data['deudas'],
                    credit_scoring=data['credit_scoring'],
                    cliente_actual=data['cliente_actual']
                )
            nuevo_cliente.save()
            return redirect('cliente_registrado')
    else:
        form = ClienteForm()
    return render(request, 'registrar_cliente.html', {'form': form})

def cliente_registrado(request):
    return render(request, 'cliente_registrado.html')

def ver_clientes(request):
    search_query = request.GET.get('search', '')
    if search_query:
        clientes = Cliente.objects.filter(
            __raw__={
                '$or': [
                    {'dni': {'$regex': search_query, '$options': 'i'}},
                    {'nombre': {'$regex': search_query, '$options': 'i'}}
                ]
            }
        )
    else:
        clientes = Cliente.objects.all()
    print(clientes)
    return render(request, 'ver_clientes.html', {'clientes': clientes})