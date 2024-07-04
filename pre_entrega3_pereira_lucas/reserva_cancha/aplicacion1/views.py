from django.shortcuts import render
from .models import *

from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion1/index.html")

def reservarcancha(request):
    contexto = {"Reservarcancha": Reservarcancha.objects.all()}
    return render(request,"aplicacion1/reservarcancha.html", contexto)

def buscarrival(request):
    contexto = {"Buscarrival": Buscarrival.objects.all()}
    return render(request, "aplicacion1/buscarrival.html", contexto)

def reservarevento(request):
    contexto = {"Reservarevento": Reservarevento.objects.all()}
    return render(request, "aplicacion1/reservarevento.html", contexto)

def contacto(request):
    return render(request, "aplicacion1/contacto.html")

def iniciasesion(request):
    return render(request, "aplicacion1/iniciasesion.html")

# buscar
def buscarCancha (request):
    return render (request, "aplicacion1/buscar.html")

def encontrarCancha (request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        busqueda = Reservarevento.objects.filter(nombre_cancha__icontains=patron)
        contexto = {"Reservarevento" : busqueda}
    else:
        contexto = {"Reservarevento" : Reservarevento.objects.all()}
        
    return render ( request, "aplicacion1/reservarevento.html", contexto)

        
        
        





# formulario

def reservarcanchaForm(request):
    if request.method == "POST":
        miForm = ReservarcanchaForm(request.POST)
        if miForm.is_valid():
            reserva_nombre = miForm.cleaned_data.get("nombre")
            reserva_numero_celular = miForm.cleaned_data.get("numero_celular")
            reserva_nombre_cancha = miForm.cleaned_data.get("nombre_cancha")
            reserva_hora_reserva = miForm.cleaned_data.get("hora_reserva")
            reserva_dia_reserva = miForm.cleaned_data.get("dia_reserva")
            reserva = Reservarcancha(nombre=reserva_nombre,numero_celular=reserva_numero_celular,nombre_cancha=reserva_nombre_cancha,hora_reserva=reserva_hora_reserva,dia_reserva=reserva_dia_reserva)
            reserva.save()
            contexto = {"Reservarcancha": Reservarcancha.objects.all()}
            return render(request,"aplicacion1/reservarcancha.html", contexto)

    else:
        miForm = ReservarcanchaForm()
        
    return render(request, "aplicacion1/reservarcanchaForm.html",{"form" : miForm} )

def buscarrivalForm(request):
    if request.method == "POST":
        miForm = BuscarrivalForm(request.POST)
        if miForm.is_valid():
            buscar_nombre_cancha = miForm.cleaned_data.get("nombre_cancha")
            buscar_hora_reserva = miForm.cleaned_data.get("hora_reserva")
            buscar_dia_reserva = miForm.cleaned_data.get("dia_reserva")
            buscar_tu_equipo = miForm.cleaned_data.get("tu_equipo")
            buscar_numero_celular = miForm.cleaned_data.get("numero_celular")
            buscar = Buscarrival(nombre_cancha=buscar_nombre_cancha,hora_reserva=buscar_hora_reserva,dia_reserva=buscar_dia_reserva,tu_equipo=buscar_tu_equipo,numero_celular=buscar_numero_celular)
            buscar.save()
            contexto = {"Buscarrival": Buscarrival.objects.all()}
            return render(request,"aplicacion1/buscarrival.html", contexto)

    else:
        miForm = BuscarrivalForm()
        
    return render(request, "aplicacion1/buscarrivalForm.html",{"form" : miForm} )

def reservareventoForm(request):
    if request.method == "POST":
        miForm = ReservareventoForm(request.POST)
        if miForm.is_valid():
            reservar_nombre_cancha = miForm.cleaned_data.get("nombre_cancha")
            reservar_hora_reserva = miForm.cleaned_data.get("hora_reserva")
            reservar_cantidad_horas = miForm.cleaned_data.get("cantidad_horas")
            reservar_dia_reserva = miForm.cleaned_data.get("dia_reserva")
            reservar_tipo_evento = miForm.cleaned_data.get("tipo_evento")
            reservar = Reservarevento(nombre_cancha=reservar_nombre_cancha,hora_reserva=reservar_hora_reserva,cantidad_horas=reservar_cantidad_horas,dia_reserva=reservar_dia_reserva,tipo_evento=reservar_tipo_evento)
            reservar.save()
            contexto = {"Reservarevento": Reservarevento.objects.all()}
            return render(request,"aplicacion1/reservarevento.html", contexto)

    else:
        miForm = ReservarcanchaForm()
        
    return render(request, "aplicacion1/reservareventoForm.html",{"form" : miForm} )