import PySimpleGUI as sg
from src.handlers import Utilidades as u

def build():

    pad = ((20,0),(0,20))

    l_cont = [
        [sg.Text("MENU", font=(u.fuente, 25), text_color= u.texto_color, background_color= u.fondo_color_cont,pad = ((0,0),(20,16)), size = (20,1), justification = "c" )],
        u.buttons("JUGAR",17,"-JUGAR-",pad = pad),
        u.buttons("CONFIGURACIONES",17,"-CONFIGURACIONES-",pad = pad),
        u.buttons("TABLA DE PUNTOS",17,"-TABLA_PUNTOS-",pad = pad),
        u.buttons("ESTADISTICAS",17,"-ESTADISTICAS-",pad = pad),
        u.buttons("AYUDA",17,"-AYUDA-",pad = pad),
        u.buttons("SALIR",17,"-SALIR-",pad = pad),
    ]

    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color= u.fondo_color_cont, element_justification="l", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))
