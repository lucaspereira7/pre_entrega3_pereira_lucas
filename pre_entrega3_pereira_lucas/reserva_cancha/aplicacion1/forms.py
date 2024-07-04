from django import forms

class ReservarcanchaForm(forms.Form):
    nombre = forms.CharField(max_length=20 , required=True)
    numero_celular = forms.IntegerField(required=True)
    nombre_cancha = forms.CharField(max_length=20 , required=True)
    hora_reserva = forms.CharField(max_length=20 , required=True)
    dia_reserva = forms.CharField(max_length=20 , required=True)

class BuscarrivalForm(forms.Form):
    nombre_cancha = forms.CharField(max_length=20)
    hora_reserva = forms.CharField(max_length=20)
    dia_reserva = forms.CharField(max_length=20)
    tu_equipo = forms.CharField(max_length=20)
    numero_celular = forms.IntegerField()


class ReservareventoForm(forms.Form):
    nombre_cancha = forms.CharField(max_length=20)
    hora_reserva = forms.CharField(max_length=20)
    cantidad_horas = forms.IntegerField()
    dia_reserva = forms.CharField(max_length=20)
    tipo_evento = forms.CharField(max_length=20)

