import PySimpleGUI as sg
from ..handlers import Utilidades as u

def build(username,puntos,nivel,puntaje_total,tiempo_total,coin_encontradas,cant_coincidencias,msj_final,bonus_tiempo,puntos_ayuda):

    l_info= [
        [sg.Text(f"Nombre: {username}", font=(u.fuente,17),pad = (0,8),background_color= u.fondo_color_cont, key = "-NOMBRE-")],
        [sg.Text(f"Puntos del {nivel}: {puntos}", font=(u.fuente,17), pad = (0,8),background_color= u.fondo_color_cont, key = "-PUNTOS_USER-")],
        [sg.Text(f"Puntos por coincidencias: {puntaje_total + puntos_ayuda}", font=(u.fuente,17), pad = (0,8),background_color= u.fondo_color_cont, key = "-PUNTOS_PARTIDA-")],
        [sg.Text(f"Puntos por ayuda: {puntos_ayuda}", font=(u.fuente,17), pad = (0,8),background_color= u.fondo_color_cont, key = "-PUNTOS_AYUDA-")],
        [sg.Text(f"Bonus por tiempo: {bonus_tiempo}", font=(u.fuente,17), pad = (0,8),background_color= u.fondo_color_cont, key = "-PUNTOS_BONUS_TIEMPO-")],
        [sg.Text(f"Total: {puntaje_total + puntos + bonus_tiempo}", font=(u.fuente,17), pad = (0,8),background_color= u.fondo_color_cont, key = "-PUNTOS_TOTAL-")],
        [sg.Text(f"concidencias econtradas: {coin_encontradas}/{cant_coincidencias}", font=(u.fuente,17),background_color= u.fondo_color_cont, pad = (0,8), key = "-COINCIDENCIAS-")],
        [sg.Text(f"Tiempo total: {tiempo_total}", font=(u.fuente,17), pad = (0,8),background_color= u.fondo_color_cont, key = "-TIEMPO_PARTIDA-")],

    ]

    l_cont = [
        [sg.Text(msj_final, font=(u.fuente,20), text_color=u.texto_color, background_color= u.fondo_color_cont, pad = ((0,0),(10,10)))],
        [sg.Column(l_info, background_color= u.fondo_color_cont, justification= "l",element_justification="l", pad=(15,0))],
        u.buttons('VOLVER A JUGAR',17,"-VOLVER_JUGAR-",pad = (15,20)) + u.buttons('IR AL MENU',17,"-VOLVER-",pad = (15,20)),
    ]

    layout = [
        [sg.Text('MemPy', font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))

