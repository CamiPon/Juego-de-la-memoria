
def disney(datos_csv, params, cant):
    #acceso a carpeta de imágenes de disney
    carpeta_imagenes_disney = "Archivos" + os.sep + "images" + os.sep + "disney"
    direccion_imagenes_disney = os.path.join(os.getcwd(), carpeta_imagenes_disney)

    promedio_total_gross = 64806282
    datos = list(filter(lambda x: (x['genre'] in params) and (int(x['total_gross']) > promedio_total_gross) , datos_csv))[0:cant]
    palabras = list(map(lambda x: x['movie_title'], datos))

    direcion_img = list(map(lambda x: direccion_imagenes_disney + os.sep + x + ".png", palabras))

    return (palabras , direcion_img)

def pokemon(datos_csv, params, cant):
    #acceso a carpeta de imágenes de pokemon
    carpeta_imagenes_pokemon = "Archivos" + os.sep + "images" + os.sep + "pokemon"
    direccion_imagenes_pokemon = os.path.join(os.getcwd(), carpeta_imagenes_pokemon)
    
    datos = list(filter(lambda x: (x['Type1'] in params) or (x['Type2'] in params), datos_csv))[0:cant]

    palabras = list(map(lambda x: x['Name'], datos))

    direcion_img = list(map(lambda x: direccion_imagenes_pokemon + os.sep + x["Numero"] + ".png", datos))

    return (palabras , direcion_img)

criterios = {
    'lunes': 
    {
        "mañana":
        {
            'criterio': 'Peliculas del genero comedia  y musical de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Adventure')
        },
        "tarde":
        {
            'criterio': 'Peliculas del genero accion y aventura de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ("Drama")
        },
    },

    'martes': 
    {
        "mañana":
        {
            'criterio': 'Peliculas del genero comedia y comedia romantica de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ("Romantic Comedy","Musical", "Comedy")
        },
        "tarde":
        {
            'criterio': 'Peliculas del genero accion y comedia de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Horror','Thriller/Suspense','Action')
        },
    },

    'miercoles': 
    {
        "mañana":
        {
            'criterio': 'Peliculas del genero accion y musical de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ("Musical","Comedy")
        },
        "tarde":
        {
            'criterio': 'Peliculas del genero comedia y aventura de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Thriller/Suspense', 'Adventure')
        },
    },

    'jueves':
    {
        "mañana":
        {
            'criterio': 'Peliculas del genero musical y aventura de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ("Adventure","Action")
        },
        "tarde":
        {
            'criterio': 'Peliculas de disney entre los años 1990 y 2000',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Grass')
        },
    },

    'viernes': 
    {
        "mañana":
        {
            'criterio': 'Peliculas de genero musical de disney',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Fire')
        },
        "tarde":
        {
            'criterio': 'Peliculas de genero Drama de disney',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Flying')
        },
    },

    'sabado':
    {
        "mañana":
        {
            'criterio': 'Peliculas de genero musical de disney',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Normal')
        },
        "tarde":
        {
            'criterio': 'Peliculas de genero Drama de disney',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Water')
        },
    },

    'domingo': 
    {
        "mañana":
        {
            'criterio': 'Peliculas de genero musical de disney',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Psychic')
        },
        "tarde":
        {
            'criterio': 'Peliculas de genero Drama de disney',
            'funcion': pokemon,
            'archivo' : 'pokemon',
            'params': ('Bug')
        },
    },
}

import datetime
from tkinter.constants import N

nro_dia = datetime.datetime.today().weekday()
hs = datetime.datetime.now().hour

semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
dia = semana[nro_dia]
turno = "mañana" if hs <= 12 else "tarde"

import csv
import os
import os.path

def abrirArchivo(arch):
    dir_carp = "Archivos" + os.sep + "data_csv"                                        
    carpeta = os.path.join(os.getcwd(), dir_carp)
    archivo = open(os.path.join(carpeta, arch + ".csv"))

    with open(os.path.join(carpeta, arch + ".csv")) as archivo:
        datos_csv = []
        for i in csv.DictReader(archivo):
            datos_csv.append(dict(i))
    return datos_csv


def setearCriterios(cant):
    # guardamos en aux el diccionario correspondiente al día y turno en el que se encuentra
    aux = criterios[dia][turno]
    # abrimos el archivo según corresponda con día y turno, y guardamos lo que contiene en datos
    datos_csv= abrirArchivo(aux['archivo'])
    # se retorna la función y el nombre del archivo utilizado
    return aux['funcion'](datos_csv,aux['params'],cant)
