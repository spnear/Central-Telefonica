import pygame
class Senalizacion:
    directorio = "/home/sebastian/PycharmProjects/CentralTelefonica/Tonos/"
    def __init__(self):
        self.botones = {1:Senalizacion.directorio+"Num1.wav",2:Senalizacion.directorio+"Num2.wav",
                        3:Senalizacion.directorio+"Num3.wav",4:Senalizacion.directorio+"Num4.wav",
                        5:Senalizacion.directorio+"Num6.wav",7:Senalizacion.directorio+"Num7.wav",
                        8:Senalizacion.directorio+"Num1.wav",9:Senalizacion.directorio+"Num9.wav",
                        0:Senalizacion.directorio+"Num0.wav"}
        self.estados = {"invitacion":Senalizacion.directorio+"invitacion.wav",
                        "noabonado":Senalizacion.directorio+"Noabonado.wav",
                        "ocupado":Senalizacion.directorio+"ocupado.wav",
                        "fs":Senalizacion.directorio+"fs.wav"}
        self.tonos = {1:Senalizacion.directorio+"ring.wav",2:Senalizacion.directorio+"ring2.wav"}

    def reproducir(self,tono):
        pygame.mixer.init()
        pygame.mixer.music.load(tono)
        pygame.mixer.music.play(1, 0)
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.stop()
