import PySimpleGUI as sg
from ..handlers import Utilidades as u
import os
import json

dir_arch = "Archivos" + os.sep +"arc_usuarios.json"
archivo = os.path.join(os.getcwd(), dir_arch)

data = [[],[],[]]

heading_1 = ['Nombre usuarie','Nivel 1']
heading_2 = ['Nombre usuarie','Nivel 2']
heading_3 = ['Nombre usuarie','Nivel 3']

def ordenar(list_):
    pos = 1
    list_length = len(list_)

    for i in range(0, list_length):
        for j in range(0, list_length-i-1):  
            if (list_[j][pos] < list_[j + 1][pos]):  
                temp = list_[j]  
                list_[j]= list_[j + 1]  
                list_[j + 1]= temp  

def generar_tabla(list_):
    tabla = []
    for elem in list_:
        aux = []
        aux.append(elem[0])
        aux.append(elem[1])
        tabla.append(aux)
    return tabla

def build_tabla():
    with open(os.path.join(archivo), "r", encoding="utf8") as arc_usuarios:
        data_usuarios = json.load(arc_usuarios)
    if len(data_usuarios) != 1:
        for elem in data_usuarios:
            if elem != "invitado":
                data[0].append((elem,data_usuarios[elem]["puntos"]["NIVEL_1"]))
                data[1].append((elem,data_usuarios[elem]["puntos"]["NIVEL_2"]))
                data[2].append((elem,data_usuarios[elem]["puntos"]["NIVEL_3"]))

        for a in data:
            ordenar(a)

        cont_tablas = [
            [sg.Table(values=generar_tabla(data[0]),headings=heading_1,justification='center',text_color= u.texto_color, background_color= u.fondo_color)] +
            [sg.Table(values=generar_tabla(data[1]),headings=heading_2,justification='center',text_color= u.texto_color, background_color= u.fondo_color)] +
            [sg.Table(values=generar_tabla(data[2]),headings=heading_3,justification='center',text_color= u.texto_color, background_color= u.fondo_color)]
        ]

    else:
        # cont_tablas = [
        #     [sg.Table(values= [],headings=heading_1,justification='center',text_color= u.texto_color, background_color= u.fondo_color)] +
        #     [sg.Table(values= [],headings=heading_2,justification='center',text_color= u.texto_color, background_color= u.fondo_color)] +
        #     [sg.Table(values= [],headings=heading_3,justification='center',text_color= u.texto_color, background_color= u.fondo_color)]
        # ]
        cont_tablas = [[sg.Text('No hay usuarios registrados, por lo tanto tampoco datos que mostrar',font=(u.fuente, 13),text_color= u.texto_color,background_color= u.fondo_color_cont)]]
    return cont_tablas

def build():

    cont_tablas = build_tabla()

    cont = [
        [sg.Text("Tablas de Puntuaciones", font=(u.fuente, 17),text_color= u.texto_color,background_color= u.fondo_color_cont, pad = ((200,200),(10,20)) )],
        [sg.Column(cont_tablas, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))],
        u.buttons('VOLVER',17,"-VOLVER-",pad = ((0,0),(25,20))),
    ]

    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color= u.texto_color ,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
        ]
    
    window = sg.Window("Tablas de Puntuaciones - Mempy", layout, font=(u.fuente,10), element_justification="c",background_color= u.fondo_color, margins = (20,20))
    
    return window