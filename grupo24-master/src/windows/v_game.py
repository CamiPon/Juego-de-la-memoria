import PySimpleGUI as sg
from ..handlers import Utilidades as u 

def build_niveles():
    layout = [u.buttons("Nivel 1",14,"-NIVEL_1-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("Nivel 2",14,"-NIVEL_2-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("Nivel 3",14,"-NIVEL_3-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("VOLVER",14,"-VOLVER-", pad =((10,10),(0,10)), size = (30,1))]

    return sg.Window("MemPy",layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))

def build(user,configuracion,nivel,ficha,puntaje_total):

    cant_casillas = configuracion["cant_casillas"][nivel]
    coincidencias = configuracion["coincidencias"]
    tiempo = configuracion["tiempo"]
    cant_ayudas = configuracion["ayudas"][1]
    total_ayudas = cant_ayudas

    dim_x, dim_y = cant_casillas.split("x")
    cant_elem = int(dim_x) * int(dim_y)
    pares = int(cant_elem / coincidencias)
    encontrados = 0
    t = '{:02d}:{:02d}'.format(tiempo // 60,tiempo % 60)
    
    l_tablero = ficha.generarTablero(cant_casillas,coincidencias)

    l_info = [
        [sg.Text("Tiempo", font=( u.fuente, 25), text_color= u.texto_color, background_color= u.fondo_color_cont,pad = ((0,0),(30,0)),)],
        [sg.Text("00:00", font=( u.fuente, 38), text_color= u.texto_color,pad = ((0,0),(0,40)), background_color=  u.fondo_color_cont, key='-TIMER-',),
        sg.Text(" / ", font=( u.fuente, 30), text_color= u.texto_color, background_color= u.fondo_color_cont,pad = ((0,0),(0,25)),),
        sg.Text("Máximo \n" + t, font=( u.fuente, 15), text_color= u.texto_color, background_color=  u.fondo_color_cont,pad = ((0,0),(0,25)))],
        [sg.Text(f"{user.username} ({user.puntos[nivel]} puntos)", font=( u.fuente, 20), text_color= u.texto_color, background_color=  u.fondo_color_cont,pad = ((0,0),(0,20)) )],
        [sg.Text(f"Puntos: {0} / {puntaje_total}      ",key='-PUNTAJE-', font=( u.fuente, 17), text_color= u.texto_color, background_color=  u.fondo_color_cont,pad = ((0,0),(0,20)))],
        [sg.Text(f"Conjuntos encontrados: {encontrados}/{pares}",key='-CONJUNTOS-', font=( u.fuente, 17), text_color= u.texto_color, background_color=  u.fondo_color_cont)],
        [sg.Text("Dificultad: " + cant_casillas, font=( u.fuente, 17), text_color= u.texto_color, background_color=  u.fondo_color_cont)],
        [sg.Button("AYUDAS ", font = ( u.fuente, 13), border_width = 1, button_color =  u.boton_color, key = "-AYUDA-", pad = ((10,10),(10,20)))]+
        [sg.Text( str(cant_ayudas) +" / " + str(total_ayudas), font=( u.fuente, 17), text_color= u.texto_color, background_color=  u.fondo_color_cont,pad = ((10,10),(10,20)), key =("-X-"))],
        [sg.Text(str("                                                        "), font=( u.fuente, 12), text_color= "#FFFF00", background_color=  u.fondo_color_cont,pad = ((10,10),(10,20)), key ="-30_SEG-")],
        [sg.Button("SALIR", font = ( u.fuente, 15), border_width = 1, button_color =  u.boton_color, key = "-SALIR-", pad = ((15,15),(10,30)), size= (20,1))],
    ]

    layout = [
        [sg.Column(l_tablero, background_color=  u.fondo_color_cont, element_justification="c", pad=((5,10),(5,5)))] +
        [sg.Column(l_info, background_color=  u.fondo_color_cont,element_justification="c", pad=((10,5),(5,5)))]
    ]

    board = sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (2,2),)
    return board
