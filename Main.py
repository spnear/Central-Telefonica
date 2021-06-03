from tkinter import *
from Abonados import Abonados
from Senalizacion import *
from Central2 import Central

"""sx = Senalizacion()
abonados = Abonados(318)
listaAbonados = abonados.generarListaAbonados(900)
(listaOcupados,listaFueraServicio) = abonados.generarEstadosAbonados(0.3,0.15)
central = Central(listaAbonados,listaOcupados,listaFueraServicio)
estado = central.buscarAbonado(318000)
if estado == 1:
    sx.reproducir(sx.estados["invitacion"])
elif estado == 2:
    sx.reproducir(sx.estados["ocupado"])
elif estado == 3:
    sx.reproducir(sx.estados["fs"])
elif estado == 4:
    sx.reproducir(sx.estados["noabonado"])
"""
mensaje = input("Introduce una cadena: ")
count = len(mensaje)
for i in str(mensaje):
    if (i.isspace()):
        count -= 1
print(count)
