from django.contrib import admin

# Register your models here.
from .models import *

class ReservarcanchaAdmin(admin.ModelAdmin):
    list_display = ("dia_reserva" , "hora_reserva" , "nombre_cancha" )
    list_filter = ( "nombre_cancha" ,)

class BuscarrivalAdmin(admin.ModelAdmin):
    list_display = ("dia_reserva" , "hora_reserva" , "nombre_cancha" , "tu_equipo")
    list_filter = ( "nombre_cancha" ,)

class ReservareventoAdmin(admin.ModelAdmin):
    list_display = ("dia_reserva" , "hora_reserva" , "nombre_cancha" , "tipo_evento" )
    list_filter = ( "nombre_cancha" ,)

admin.site.register(Reservarcancha , ReservarcanchaAdmin)
admin.site.register(Buscarrival , BuscarrivalAdmin)
admin.site.register(Reservarevento , ReservareventoAdmin)
