import PySimpleGUI as sg
from src.handlers import Utilidades as u

def build():

    l_cont_form = [
        u.texts("Usuario",17),
        [sg.InputText('',font = ( u.fuente), size=(35,1),pad = ((0,0),(0,10)), key = "-USERNAME-" )],
        u.texts("Contraseña",17),
        [sg.InputText('',font = ( u.fuente), password_char = "*", size=(35,1),pad = ((0,0),(0,0)), key = "-PASSW-" )],
    ]

    l_cont = [
        u.texts("Inicio de Sesion",25,pad =((62,62),(20,16))),
        [sg.Column(l_cont_form, background_color= u.fondo_color_cont,element_justification="l", pad=(0,0))],
        u.buttons('INICIAR SESION',17,"-INICIAR_SESION-",pad = ((0,0),(15,25))),
        u.texts("¿Sos nuevo?",15,pad = (0,10)),
        u.buttons('REGISTRARSE',17,"-REGISTRARSE-",pad = (0,9)),
        u.buttons('ENTRAR COMO INVITADO',0,"-ENTRAR_INVITADO-",pad = ((0,0),(0,20))),
    ]

    layout = [
        [sg.Text('MemPy', font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))
