from django.db import models

# Create your models here.

class Inicia_sesion(models.Model):
    nombre = models.CharField(max_length=20)
    numero_celular = models.IntegerField()
    email = models.EmailField()

class Reservarcancha(models.Model):
    nombre = models.CharField(max_length=20)
    numero_celular = models.IntegerField()
    nombre_cancha = models.CharField(max_length=20)
    hora_reserva = models.CharField(max_length=20)
    dia_reserva = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Cancha reservada"
        verbose_name_plural = "Canchas reservadas"
        ordering = ["dia_reserva","hora_reserva"]

    def __str__(self):
        return f"{self.dia_reserva},{self.hora_reserva}"



class Buscarrival(models.Model):
    nombre_cancha = models.CharField(max_length=20)
    hora_reserva = models.CharField(max_length=20)
    dia_reserva = models.CharField(max_length=20)
    tu_equipo = models.CharField(max_length=20)
    numero_celular = models.IntegerField()

    class Meta:
        verbose_name = "Buscar rival"
        ordering = ["dia_reserva","hora_reserva"]

    def __str__(self):
        return f"{self.dia_reserva},{self.hora_reserva}"

class Reservarevento(models.Model):
    nombre_cancha = models.CharField(max_length=20)
    hora_reserva = models.CharField(max_length=20)
    cantidad_horas = models.IntegerField()
    dia_reserva = models.CharField(max_length=20)
    tipo_evento = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Reserva de evento"
        ordering = ["dia_reserva","hora_reserva"]

    def __str__(self):
        return f"{self.tipo_evento},{self.dia_reserva},{self.hora_reserva}"