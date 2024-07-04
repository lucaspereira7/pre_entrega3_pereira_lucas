from django.urls import path,include
from .views import *


urlpatterns = [
    path ('',home,name="home"),
    path ('buscarrival/', buscarrival, name="buscarrival"),
    path ('reservarcancha/', reservarcancha, name="reservarcancha"),
    path ('reservarevento/', reservarevento, name="reservarevento"),
    path ('contacto/', contacto, name="contacto"),
    path ('iniciasesion/', iniciasesion, name="iniciasesion"),
    #formularios
    path ('reservarcanchaForm/', reservarcanchaForm, name="reservarcanchaForm"),
    path ('buscarrivalForm/', buscarrivalForm, name="buscarrivalForm"),
    path ('reservareventoForm/', reservareventoForm, name="reservareventoForm"),
    #buscar
    path ('buscarCancha/', buscarCancha, name="buscarCancha"),
    path ('encontrarCancha/', encontrarCancha, name="encontrarCancha"),


] 
