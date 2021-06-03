from  tkinter import *
import random
import winsound
from tkinter import messagebox
b = [-1]
class Central():
    def __init__(self):
        self.num = b
        self.primerNum=False

    def abon(self):
        self.abonados = list(range(8380000,8380900))
        self.disponibles = random.sample(self.abonados, 585)
        self.abonados = set(self.abonados) - set(self.disponibles)
        self.ocupados = random.sample(self.abonados, 225)
        self.abonados = set(self.abonados) - set(self.ocupados)
        self.outser = random.sample(self.abonados, 90)
        #return print("Los numeros disponibles son:{0}\nLos numeros ocupados son:{1}\nLos numeros fuera de servicio son:{2}".format(self.disponibles,self.ocupados,self.outser))
        return ("Los abonados",self.disponibles)
    def numero(self):
        print('El numero marcado es:', self.num)
        print("El estado disponible es: ", a.estadoDis())
        print("El estado ocupado es: ", a.estadoOc())
        print("El estado fuera de servicio es: ", a.estadoFue())
        x = a.estadoDis()
        y = a.estadoOc()
        z = a.estadoFue()
        if self.num < [8380001] or self.num > [8380900]:
            winsound.PlaySound("errada", winsound.SND_FILENAME)
        else:
            if x == True:
                print("Establaciendo llamada")
                winsound.PlaySound("tono", winsound.SND_FILENAME)
            if y == True:
                print("Numero ocupado")
                winsound.PlaySound("ocupado", winsound.SND_FILENAME)
            if z == True:
                print("Numero fuera de servicio")
                winsound.PlaySound("fueraS", winsound.SND_FILENAME)
        return self.num

    def estadoDis(self):
        c=self.num[0]
        if c in self.disponibles:
            self.estadoDisponible = True
            return self.estadoDisponible
        else:
            self.estadoDisponible = False
            return self.estadoDisponible
    def estadoOc(self):
        c = self.num[0]
        if c in self.ocupados:
            self.estadoOcupado = True
            return self.estadoOcupado
        else:
            self.estadoOcupado = False
            return self.estadoOcupado
    def estadoFue(self):
        c = self.num[0]
        if c in self.outser:
            self.estadoFuera = True
            return self.estadoFuera
        else:
            self.estadoFuera = False
            return self.estadoFuera

class Senalizacion():
    def __init__(self):
        self.numero=[]
    def tonosMarcacion(self,num1):
        tonos={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",0:"cero"}
        t=tonos[num1]
        winsound.PlaySound(t, winsound.SND_FILENAME)


raiz = Tk()
raiz.title("Central Telefonica")
miFrame = Frame()
w = Label(raiz, text=a.abon(),bd=1,relief="solid",width=220,height=1)
w.pack()
miFrame.pack()
numeroPantalla = StringVar()

#--Funcion teclas--
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)

def cargar(num):
    c = int(num)
    #print("El numero ingresado es:" , c)
    b.pop()
    b.append(c)
    #numeroPantalla.set(num)
    #return c

def borrar():
    numeroPantalla.set("")

#--Pantalla--
pantalla = Entry(miFrame, textvariable=numeroPantalla, insertwidth=.1, font=30)
pantalla.grid(row=1, column=1, padx=5,pady=5,columnspan=4)
pantalla.config(background='white', justify='center')
#--Botones--
botoncar=Button(miFrame, padx=16, pady=16, text='Llamar', width=10, font=30 , command=lambda:[cargar(numeroPantalla.get()),a.numero()])
botoncar.grid(row=3, column=4)
#botonnum=Button(miFrame, text='Num', width=10, command=lambda:a.numero())
#botonnum.grid(row=4, column=4)
botondel=Button(miFrame, padx=16, pady=16, text='Borrar', width=10, font=30 , command=lambda:borrar())
botondel.grid(row=5, column=4)
boton1=Button(miFrame, padx=16, pady=16, text='1', width=10, font=30 , command=lambda:[numeroPulsado("1"),c.tonosMarcacion(1)])
boton1.grid(row=2, column=1)
boton2=Button(miFrame, padx=16, pady=16, text='2', width=10, font=30 , command=lambda:[numeroPulsado("2"),c.tonosMarcacion(2)])
boton2.grid(row=2, column=2)
boton3=Button(miFrame, padx=16, pady=16, text='3', width=10, font=30 , command=lambda:[numeroPulsado("3"),c.tonosMarcacion(3)])
boton3.grid(row=2, column=3)
boton4=Button(miFrame, padx=16, pady=16, text='4', width=10, font=30 , command=lambda:[numeroPulsado("4"),c.tonosMarcacion(4)])
boton4.grid(row=3, column=1)
boton5=Button(miFrame, padx=16, pady=16, text='5', width=10, font=30 , command=lambda:[numeroPulsado("5"),c.tonosMarcacion(5)])
boton5.grid(row=3, column=2)
boton6=Button(miFrame, padx=16, pady=16, text='6', width=10, font=30 , command=lambda:[numeroPulsado("6"),c.tonosMarcacion(6)])
boton6.grid(row=3, column=3)
boton7=Button(miFrame, padx=16, pady=16, text='7', width=10, font=30 , command=lambda:[numeroPulsado("7"),c.tonosMarcacion(7)])
boton7.grid(row=4, column=1)
boton8=Button(miFrame, padx=16, pady=16, text='8', width=10, font=30 , command=lambda:[numeroPulsado("8"),c.tonosMarcacion(8)])
boton8.grid(row=4, column=2)
boton9=Button(miFrame, padx=16, pady=16, text='9', width=10, font=30 , command=lambda:[numeroPulsado("9"),c.tonosMarcacion(9)])
boton9.grid(row=4, column=3)
boton9=Button(miFrame, padx=16, pady=16, text='0', width=10, font=30 , command=lambda:[numeroPulsado("0"),c.tonosMarcacion(0)])
boton9.grid(row=5, column=2)

miFrame.mainloop()
