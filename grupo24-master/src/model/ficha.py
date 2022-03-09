import PySimpleGUI as sg
from src.handlers import criterios
import random
import os
import os.path

class Fichas:
    def _init_(self):
        self.lista = []
        self.conjunto = 0

    def generarTablero(self,dim,coincidencias):

        self.lista =  []
        dim_x, dim_y = dim.split("x")
        cant_elem = int(dim_x) * int(dim_y)
        self.conjunto = int(cant_elem / coincidencias)
        
        #traemos los elementos del archivo csv y los colocamos en una lista. También se trabaja diferente según el archivo utilizado
        ficha_criterios= criterios.setearCriterios(self.conjunto)

        #inicialización de lista a desordenar y de j que se utiliza para el acceso a los elementos de lista
        li = []
        j = 0

        #acceso a carpeta de imágenes
        carpeta_imagenes = "Archivos" + os.sep + "images"   
        direccion_imagenes = os.path.join(os.getcwd(), carpeta_imagenes) 

        for c in range(self.conjunto):
            for a in range(coincidencias):
                li.append({
                    "frente" : ficha_criterios[1][j],
                    "dorso" : direccion_imagenes + os.sep + "dorso.png",
                    "palabra" : (ficha_criterios[0][j],direccion_imagenes + os.sep + "fondo.png"),})
            j += 1

        #desordenamos los elementos
        random.shuffle(li)

        #agregamos los elementos desordenados en la lista/matriz
        i=0
        for y in range(int(dim_y)):
            l = []
            for x in range(int(dim_x)):
                l.append(li[i])
                i += 1
            self.lista.append(l)
                
        l_tablero = []
        for y in range(int(dim_x)):
            l_tablero += [[sg.Button("                 ",image_filename= self.lista[x][y]["dorso"], image_size=(110,110), image_subsample=3,  key=f"cell-{x}-{y}") for x in range(int(dim_y))]]
        return l_tablero


    def mostrarFrente(self, window, tipo_elementos, x, y):
        if tipo_elementos == "Imagenes":
            window[f"cell-{x}-{y}"].Update(image_filename = self.lista[x][y]["frente"], image_size=(110,110), image_subsample=3)
        else:
            window[f"cell-{x}-{y}"].Update(self.lista[x][y]["palabra"][0],image_filename= self.lista[x][y]["palabra"][1],image_size=(110,110))

    def mostrarDorso(self, window, key):
        for i in range(len(key)):
            x, y =  key[i]
            window[f"cell-{x}-{y}"].Update("                 ",image_filename = self.lista[x][y]["dorso"], image_size=(110,110), image_subsample=3,disabled = False)

    def ayuda(self,window,fichasEncontradas,tipo_elementos):
        max_x = len(self.lista)
        max_y = len(self.lista[0])

        x = random.randrange(0, max_x)
        y = random.randrange(0, max_y)
        while (x,y) in fichasEncontradas:
            x = random.randrange(0, max_x)
            y = random.randrange(0, max_y)

        self.mostrarFrente(window, tipo_elementos, x, y)

        return x, y