import PySimpleGUI as sg
from src.handlers import Utilidades as u

pad = ((20,20),(20,20))

def build():

    cont = [
        [sg.Text("Estadisticas", font=(u.fuente,20), text_color=u.texto_color, background_color= u.fondo_color_cont, pad = ((0,0),(15,10)))],
        u.buttons('Top 10 de palabras',17,"-TOP-",pad = ((20,20),(20,20))),
        u.buttons('Porcentaje por estado',17,"-PORCENTAJE_ESTADO-",pad = ((20,20),(0,20))),
        u.buttons('Porcentaje por género',17,"-PORCENTAJE_GENERO-",pad = ((20,20),(0,20))),
        u.buttons('VOLVER',17,"-VOLVER-",pad = ((135,135),(25,20))),
    ]

    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
    ]

    return sg.Window("Estadísticas", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))