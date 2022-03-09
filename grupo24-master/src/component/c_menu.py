from src.windows import v_menu
from src.windows import v_ayuda
from src.component import c_configuraciones
from src.component import c_game
from src.component import c_puntaje
from src.component import c_estadisticas
import PySimpleGUI as sg


def start(user):
    window = loop(user)
    window.close()

def loop(user):
    window = v_menu.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-SALIR-"):
            break
        
        if event == "-CONFIGURACIONES-":
            window.close()
            #window.hide()
            c_configuraciones.start(user)
            #window.un_hide()
            window = v_menu.build()
        if event == "-JUGAR-":
            window.hide()
            c_game.start(user)
            window.un_hide()
        if event == "-TABLA_PUNTOS-":
            window.hide()
            c_puntaje.start()
            window.un_hide()
        if event == "-ESTADISTICAS-":
            window.hide()
            c_estadisticas.start()
            window.un_hide()
        if event == "-AYUDA-":
            window.hide()
            v_ayuda.start()
            window.un_hide()
    return window