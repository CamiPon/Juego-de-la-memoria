from abc import abstractmethod, ABC
from ..handlers import Utilidades
import json
import os

dir_carp = "Archivos"
dir_arch = "arc_configuracion.json"
carpeta = os.path.join(os.getcwd(), dir_carp)

text = {"Comienzo": "Ahora comienza la partida",
        "Gano": "¡Ganaste!",
        "Perdio":"¡Perdiste!",
        "Quedan 30 segundos": "¡Quedan menos de 30 segundos!"
        }
casillas_nivel = { 
    "NIVEL_1": "4x2",
    "NIVEL_2": "4x4",
    "NIVEL_3": "6x3"
    }

class configuracion():
    def __init__(self,textos = text, cant_casillas = casillas_nivel, coincidencias = 2, tiempo = 65, estilo = "t1", tipo_elementos = "Imagenes", ayudas = (True,3)):
        self.textos = textos
        self.cant_casillas = cant_casillas
        self.coincidencias = coincidencias
        self.tiempo = tiempo
        self.estilo = estilo
        self.tipo_elementos = tipo_elementos
        self.ayudas = ayudas
    @abstractmethod        
    def getUserName(self):
        raise NotImplementedError
    def guardarConfigJson(self):
        """Esta función abre el archivo json donde se encuentran guardadas las configuraciones
        y devuelve en data_configuracion la estructura allí guardada, en caso de no haber nada en
        el archivo, crea un nuevo diccionario. Luego modifica la estructura recibida y 
        sobrescribe el archivo"""
        username = self.getUserName()
        try:
            with open(os.path.join(carpeta, dir_arch), "r", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion= {}
        with open(os.path.join(carpeta, dir_arch), "w", encoding="utf8") as file:
            data_configuracion[username] = {
                "textos" : self.textos,
                "cant_casillas" : self.cant_casillas,
                "coincidencias" : self.coincidencias,
                "tiempo" : self.tiempo,
                "estilo" : self.estilo,
                "tipo_elementos" : self.tipo_elementos,
                "ayudas" : self.ayudas,
                }   
            json.dump(data_configuracion,file, indent=4, ensure_ascii=False)

    def buscarConfig(self):
        username = self.getUserName()
        with open(os.path.join(carpeta, dir_arch), "r", encoding="utf8") as arc_configuracion:
            data_configuracion = json.load(arc_configuracion)
            self.textos = data_configuracion[username]["textos"]
            self.cant_casillas = data_configuracion[username]["cant_casillas"]
            self.coincidencias = data_configuracion[username]["coincidencias"]
            self.tiempo = data_configuracion[username]["tiempo"]
            self.estilo = data_configuracion[username]["estilo"]
            self.tipo_elementos = data_configuracion[username]["tipo_elementos"]
            self.ayudas = data_configuracion[username]["ayudas"]
        Utilidades.start(self.estilo)

    def configActual(self):
        """Esta función abre el archivo json donde se encuentran guardadas las configuraciones
        y devuelve en data_configuracion la estructura allí guardada, en caso de no haber nada en
        el archivo, crea un nuevo diccionario. Luego guarda en la clase actual lo recibido en data_configuracion
        y lo devuelve."""
        conf = {
            "textos": self.textos,
            "cant_casillas": self.cant_casillas,
            "coincidencias": self.coincidencias,
            "tiempo": self.tiempo,
            "estilo": self.estilo,
            "tipo_elementos": self.tipo_elementos,
            "ayudas": self.ayudas
        }
        return conf
    
    def setConfig(self,conf):
        """Esta función setea las variables de clase con lo recibido en los parámetros"""
        self.textos = conf.textos
        self.cant_casillas = conf.cant_casillas
        self.coincidencias = conf.coincidencias
        self.tiempo = conf.tiempo
        self.estilo = conf.estilo
        self.tipo_elementos = conf.tipo_elementos
        self.ayudas = conf.ayudas
        Utilidades.start(self.estilo)

    def imprimirConfig(self):
        """Esta función imprime los valores de las variables de clase"""
        print(self.cant_casillas)
        print(self.coincidencias)
        print(self.tipo_elementos)
        print(self.estilo)
        print(self.tiempo)
        print(self.textos)
