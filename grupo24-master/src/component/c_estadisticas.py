import PySimpleGUI as sg
from ..handlers import estadisticas as estad
from ..windows import v_estadisticas

def start():
    window = loop()
    window.close()

def loop():
    window = v_estadisticas.build()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED,"Exit","-VOLVER-"):
            break
        if event == "-TOP-":
            estad.Top10Palabras()
        if event == "-PORCENTAJE_ESTADO-" :
            estad.porcentajeEstados()
        if event == "-PORCENTAJE_GENERO-" :
            estad.porcentajeGenero()
    return window