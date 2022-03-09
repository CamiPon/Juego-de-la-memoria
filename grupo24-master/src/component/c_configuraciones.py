from src.windows import v_configuraciones
from src.model.configuracion import configuracion
import PySimpleGUI as sg


def start(user):
    window = loop(user)
    window.close()

def loop(user):
    conf = user.configActual()
    window = v_configuraciones.build(conf)
    texto = conf["textos"]

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break

        if values["-AYUDAS-"]:
            window["-AYUDAS_CANT-"].update(visible=True)
        else:
            window["-AYUDAS_CANT-"].update(visible=False)

        if values["-coinc2-"]:
            window["-CASILLAS_1-"].update("4x2", values = ["4x2","4x3"], size = (8,1) )
            window["-CASILLAS_2-"].update("4x4", values = ["4x4","6x2"], size = (8,1) )
            window["-CASILLAS_3-"].update("6x3", values = ["6x3","6x4"], size = (8,1) )

        if values["-coinc3-"]:
            window["-CASILLAS_1-"].update("3x4", values = ["3x4","3x5"], size = (8,1) )
            window["-CASILLAS_2-"].update("3x6", values = ["3x6","3x7"], size = (8,1) )
            window["-CASILLAS_3-"].update("6x5", values = ["6x5","6x6"], size = (8,1) )
            
        if event == "-TEXTOS-":
            window["-TXTACTUAL-"].update(texto[values["-TEXTOS-"]])

        if event == "-APLITEXTOS-":
            if len(values["-TXTACTUAL-"]) < 35:
                texto[values["-TEXTOS-"]] = values["-TXTACTUAL-"]
                sg.popup("Texto modificado")
            else:
                sg.popup("El Texto modificado supera los 35 caracteres")

        if event == "-GUARDAR-":
            casillas = {
                "NIVEL_1": values["-CASILLAS_1-"],
                "NIVEL_2": values["-CASILLAS_2-"],
                "NIVEL_3": values["-CASILLAS_3-"]
            }

            ayudas = ( values["-AYUDAS-"], values["-AYUDAS_CANT-"])

            cant_coinci = 2 if values["-coinc2-"] else 3

            user.setConfig(configuracion(texto , casillas, cant_coinci, values["-TIEMPO-"], values["-ESTILO-"], values["-ELEMENTOS-"], ayudas))
            user.guardarConfigJson()
            break
    return window