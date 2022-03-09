import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
from pandas.core.series import Series
matplotlib.use('TkAgg')
from collections import Counter
from src.handlers import Utilidades as u

dir_carp = "Archivos" + os.sep + "data_csv" + os.sep + "registro.csv"
dir_archivo = os.path.join(os.getcwd(), dir_carp)

cont = pd.read_csv(dir_archivo, encoding='utf-8')

cant_partidas = cont["Partida"].unique()

import datetime
nro_dia = datetime.datetime.today().weekday()
semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
dia = semana[nro_dia]

def abrirArchivo():
    '''Esta función abre el archivo donde se encuentran registrados los eventos de las partidas y devuelve su contenido'''
    contenido = list()
    with open(os.path.join(dir_archivo), 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip('\'').split(',')
            contenido.append(columnas)
    return contenido


def guardarEnArchivo(datos):
    '''Esta función guarda en el registro de jugadas los nuevos eventos ocurridos en la partida'''
    contenido = list()
    for linea in datos:
        contenido.append(','.join(linea))
    with open(os.path.join(dir_archivo), 'w') as archivo:
        archivo.writelines(contenido)
        

def guardarEstadistica(datos,tiempo,partida,total_palabras_adivinar,evento,username,genero,edad,estado,nivel,palabra = ''):
    if username != "invitado":
        registro = [str(tiempo), str(partida), str(total_palabras_adivinar), evento, username, genero, edad, estado, palabra, nivel, dia + '\n']
        datos.append(registro)


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def Top10Palabras():
    if len(cont) != 0:
        palabras = []
        for aux in cant_partidas:
            serie = cont["Palabra"][(cont["Partida"] == int(aux)) & (cont["Estado"] == "ok")][0:1]
            for a in serie.keys():
                palabras.append(serie[a])
        a = Counter(palabras).most_common(10)

        layout_1 = [
            u.texts("Top de 10",17,pad = ((0,0),(20,0))),
            u.texts("palabras que se encuentran primero",17,pad = ((50,50),(0,15)))]

        i = 0
        for elem in a:
            layout_1.append(u.texts(str(i) + ' - ' + f'{elem[0]}',13,pad = ((10,10),(10,10))))
            i += 1
    else:
        layout_1 = [[sg.Text('No hay estados registrados, por lo tanto tampoco datos que mostrar',font=(u.fuente, 13),text_color= u.texto_color,background_color= u.fondo_color_cont)]]
    layout_1.append(u.buttons('VOLVER',13,"-VOLVER-",pad = ((62,62),(20,16))))
    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(layout_1, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
    ]
    window = sg.Window('Top 10 palabras',layout,background_color= u.fondo_color,finalize=True,element_justification='center',font='Helvetica 18',margins = (20,20))

    event,values = window.read()

    if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
        window.close()


def porcentajeEstados():
    if len(cont) != 0:
        cant_estados = cont["Estado"][ (cont["Estado"] == "abandonada") | (cont["Estado"] == "timeout") | (cont["Estado"] == "finalizada") ].value_counts()
        
        cant_timeout = cant_estados["timeout"] if "timeout" in cant_estados.keys() else 0
        cant_abandonada = cant_estados["abandonada"] if "abandonada" in cant_estados.keys() else 0
        cant_finalizada = cant_estados["finalizada"] if "finalizada" in cant_estados.keys() else 0

        etiquetas = ["Time out","Abandonada", "Finalizada"]
        data = [cant_timeout,cant_abandonada,cant_finalizada]
        fig = plt.figure()
        plt.pie(data,labels=etiquetas,autopct='%1.1f%%', startangle=90, labeldistance= 1.1)
        plt.axis('equal')
        plt.legend(etiquetas)
        plt.title("Porcentajes de partidas por estado")
        
        layout = [[sg.Canvas(key='-CANVAS-')],u.buttons('VOLVER',13,"-VOLVER-",pad = ((0,0),(10,20)))]
        window = sg.Window('Procentajes por estado',layout,background_color= u.fondo_color,finalize=True,element_justification='center',font='Helvetica 18',location=(300,100))

        draw_figure(window['-CANVAS-'].TKCanvas, fig)
    else:
        layout = [[sg.Text('No hay estados registrados, por lo tanto tampoco datos que mostrar',font=(u.fuente, 13),text_color= u.texto_color,background_color= u.fondo_color)],
        u.buttons('VOLVER',13,"-VOLVER-",pad = ((0,0),(10,20)))]
        window = sg.Window('Procentajes por estado',layout,background_color= u.fondo_color,finalize=True,element_justification='center',font='Helvetica 18',location=(300,100))

    event,values = window.read()

    if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
        window.close()


def porcentajeGenero():
    if len(cont) != 0:
        cant_ = cont["Usuarie-genero"][cont["Estado"] == "finalizada"].value_counts()

        cant_masculino = cant_["Masculino"] if "Masculino" in cant_.keys() else 0
        cant_femenino = cant_["Femenino"] if "Femenino" in cant_.keys() else 0
        cant_no_binarie = cant_["No binarie"] if "No binarie" in cant_.keys() else 0
            
        etiquetas = ["Femenino", "Masculino", "No binarie"]
        data = [cant_femenino,cant_masculino,cant_no_binarie]
        fig = plt.figure()
        plt.pie(data,labels=etiquetas,autopct='%1.1f%%', startangle=90, labeldistance= 1.1)
        plt.axis('equal')
        plt.legend(etiquetas)
        plt.title("Porcentajes de partidas finalizadas según género")
        
        layout = [[sg.Canvas(key='-CANVAS-')],u.buttons('VOLVER',13,"-VOLVER-",pad = ((0,0),(10,20)))]
        window = sg.Window('Procentajes por género',layout,background_color= u.fondo_color,finalize=True,element_justification='center',font='Helvetica 18',location=(300,100))

        draw_figure(window['-CANVAS-'].TKCanvas, fig)

    else:
        layout = [[sg.Text('No hay estados registrados, por lo tanto tampoco datos que mostrar',font=(u.fuente, 13),text_color= u.texto_color,background_color= u.fondo_color)],
        u.buttons('VOLVER',13,"-VOLVER-",pad = ((0,0),(10,20)))]
        window = sg.Window('Procentajes por género',layout,background_color= u.fondo_color,finalize=True,element_justification='center',font='Helvetica 18',location=(300,100))


    event,values = window.read()

    if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
        window.close()