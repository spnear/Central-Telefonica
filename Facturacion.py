import os,time,random
class Facturacion:
    direccion = "/home/sebastian/PycharmProjects/CentralTelefonica/"
    inicioLlamada = ''
    def __init__(self,tarifa1,tarifa2):
        self.tiempoInicial = 0
        self.tiempoFinal = 0
        self.tarifa = tarifa1
        self.tarifa2 = tarifa2
        self.segundos = 0
        self.cobro = 0
        self.acumulador = 0
        self.registro = []

    def iniciarFacturacion(self):
        self.tiempoInicial = time.time()
        Facturacion.inicioLlamada = time.strftime("%d/%m/%y %H:%M:%S")

    def terminarFacturacion(self):
        self.tiempoFinal = time.time()
        self.segundos = self.tiempoFinal - self.tiempoInicial
        self.cobro = self.segundos * self.tarifa
        self.acumulador = self.acumulador + self.cobro # Ahora terminar Facturacion me calcula cobro y me monta una acumulador


    def generarFactura(self,destinatario,remitente): # Este es el del registro en csv, podriamos llamarlo generarBaseDatos...
                                                     # MUY IMPORTANTE, ESTE ME VA AÑADIENDO LAS LLAMADAS AL CSV Y A UNA LISTA
                                                     #LA LISTA LA USO MAS ADELANTE EN LA FACTURA DEFINITIVA
        if os.path.exists(Facturacion.direccion+"factura.csv"):
            f = open(Facturacion.direccion+"factura.csv",'+a')
        else:
            f = open(Facturacion.direccion+"factura.csv",'+w')

        f.write("\n" + Facturacion.inicioLlamada)
        f.write(",Numero remitente: " + str(remitente))
        f.write(",Numero destino: " + str(destinatario))
        f.write(",segundos: {0:.2f}".format(self.segundos))
        f.write(",tarifa: " + str(self.tarifa) + "$")
        f.write(",total: {0:.2f}".format(self.cobro) + "$")
        f.close()
        self.registro.append(Facturacion.inicioLlamada+" Destinatario: "+str(destinatario)
                             +" Duración: {0:.2f} ".format(self.segundos)+"Total: {0:.2f}$".format(self.cobro))

    def generarCobroMsj(self,mensaje,destinatario,remitente): #Sería bueno borrar esto, ustedes diran
        if os.path.exists(Facturacion.direccion+str(remitente)+"factura.csv"):
            f = open(Facturacion.direccion+"factura.csv",'+a')
        else:
            f = open(Facturacion.direccion+"factura.csv",'+w')

        count = len(mensaje)
        for i in str(mensaje):
            if (i.isspace()):
                count -= 1

        f.write("\n" + time.strftime("%d/%m/%y %H:%M:%S"))
        f.write(",Numero remitente: " + str(remitente))
        f.write(",Numero destino: " + str(destinatario))
        f.write(",Cantidad letras: " + str(count))
        f.write(",tarifa: " + str(self.tarifa2) + "$")
        f.write(",total: {0:.2f}".format(count*self.tarifa2) + "$")
        f.close()
        self.acumulador = self.acumulador + count*self.tarifa2


    def generarFacturaFinal(self,remitente): # FACTURACIÓN, INGRESAR REMITENTE PARA GENERAR FACTURA
        if os.path.exists(Facturacion.direccion+str(remitente)+"factura.csv"):
            f = open(Facturacion.direccion+str(remitente)+"factura.txt",'+a')
        else:
            f = open(Facturacion.direccion+str(remitente)+"factura.txt",'+w')

        # NO TOCAR CODIGO ASCII
        f.write("=========================================================================\n"
                "                _____ _                      _____       _\n"
                "               | ___ \ |                    /  __ \     | |\n"
                "               | |_/ / |__   ___  _ __   ___| /  \/ ___ | |\n"
                "               |  __/| '_ \ / _ \| '_ \ / _ \ |    / _ \| |\n"
                "               | |   | | | | (_) | | | |  __/ \__/\ (_) | |\n"
                "               \_|   |_| |_|\___/|_| |_|\___|\____/\___/|_|\n\n"
                "                                    Telefonía para tod@s\n\n\n")

        f.write("FACTURA N°{0}                                  USUARIO:{1}\n\n\n".format(random.randint(0,9)
                                                               *100000+random.randint(0,9)*10000+random.randint(0,9)*1000
                                                               +random.randint(0,9)*100
                                                               +random.randint(0,9)*10+random.randint(0,9),remitente))
        f.write("                                       Fecha de vencimiento: {0}/{1}/{2}\n"
                "                                       Número para pagos: 34477001\n"
                "HISTORIAL DE LLAMADAS.\n".format(random.randint(0,31),random.randint(0,12),2018))

        #EL NUMERO ALEATORIO ES PARA GENERAR UN N° DE LA FACTURA CUALQUIERA, COMO PARA LA CARRETA
        for i in range(len(self.registro)):
            f.write(str(self.registro[i])+"\n")
        f.write("\n\n\n\n                                                TOTAL A PAGAR: {0:.2f}$".format(self.acumulador)+"\n")
        f.write("=========================================================================")




Fact = Facturacion(1000,10)
####################### -> Inicia la llamada
Fact.iniciarFacturacion()
time.sleep(2)
Fact.terminarFacturacion() #-> Termina llamada
Fact.generarFactura(877777,86256546)
Fact.generarCobroMsj("Pru5, hola",32154,3154)
Fact.iniciarFacturacion()
time.sleep(5)
Fact.terminarFacturacion() #-> Termina llamada
Fact.generarFactura(877777,86256546)
Fact.generarCobroMsj("Pru5, hola",32154,3154)
Fact.generarFacturaFinal(877777)

