import PySimpleGUI as sg
from ..handlers import Utilidades as u


texto1 = "Se genera un tablero que contiene fichas boca abajo. El jugador debe seleccionar 2 o 3 fichas (según la configuración) que se daran vuelta mostrando su frente, si tienen el mismo dibujo o palabra, obtienen puntos por coincidencia, si por el contrario no coinciden se dan vuelta automáticamente. Esto se repite hasta que se encuentren todas las coincidencias."

texto2 = "Al pedir una ayuda, se mostrara el frente de una ficha aleatoriamente, pasaran 2 segundos y volverá a darse vuelta las ayudas no son ilimitadas, se puede elegir la cantidad desde configuraciones con un máximo de 7 ayudas."

texto3 = "Por encontrar una coincidencia de 2 o 3 fichas se suman 10, 20 o 30 segun el nivel del juego se resta 5 puntos, por cada vez que se pide una ayuda si fanalizaste la partida antes de la mitad del tiempo sumas 100 puntos, si finalizaste antes de los 3/4 de tiempo sumas 75 puntos y si finalizaste despues de los 3/4 de tiempo sumas 50 puntos. Si no ganaste el juego por falta de tiempo o abandonaste la partida no sumaras puntos."


def build():

    text_cont = [
        u.texts("REGLAS DEL JUEGO:",17,pad =((15,0),(20,0))),
        [sg.Text(texto1, font=(u.fuente, 13), text_color= u.texto_color, background_color= u.fondo_color_cont, pad = ((15,15),(0,0)), size = (60, 5) ,auto_size_text = True)],
        u.texts("AYUDAS:",17,pad =((15,0),(15,0))),
        [sg.Text(texto2, font=(u.fuente, 13), text_color= u.texto_color, background_color= u.fondo_color_cont, pad = ((15,15),(0,0)), size = (60, 4) ,auto_size_text = True)],
        u.texts("METODO DE PUNTAJE:",17, pad = ((15,0),(15,0))),
        [sg.Text(texto3, font=(u.fuente, 13), text_color= u.texto_color, background_color= u.fondo_color_cont, pad = ((15,15),(0,0)), size = (60, 6) ,auto_size_text = True)],
    ]

    cont = [
        [sg.Column(text_cont, background_color= u.fondo_color_cont, element_justification="l", pad=(0,0))],
        u.buttons('VOLVER',17,"-VOLVER-",pad = ((0,0),(30,25))),

    ]

    layout = [
        [sg.Text('MemPy', font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))

def start():
    window = build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit","-VOLVER-"):
            break

    window.close()