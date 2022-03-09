from src.windows import v_puntaje
import PySimpleGUI as sg
def start():
    window = loop()
    window.close()

def loop():
    window = v_puntaje.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break

    return window