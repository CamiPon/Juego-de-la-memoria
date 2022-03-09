import csv
import os
import os.path
import string

dir_carp = "Archivos" + os.sep + "data_csv"                                        
carpeta = os.path.join(os.getcwd(), dir_carp)
archivo = open(os.path.join(carpeta, "pokemon.csv"))
i = 0
contenido = list()
with open(os.path.join(carpeta, "pokemon.csv"), 'r') as archivo:
    for linea in archivo:
        aux = linea.strip(string.punctuation)
        columnas = aux.split(',')
        columnas[3] = str(i)
        i += 1
        print(','.join(columnas))
        contenido.append(','.join(columnas) + '\n')

with open(os.path.join(carpeta, "pokemon.csv"), 'w') as archivo:
    archivo.writelines(contenido)