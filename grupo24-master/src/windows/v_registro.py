import PySimpleGUI as sg
from ..handlers import Utilidades as u

def build():

    l_cont_form = [
        u.texts("Usuario *",17),
        [sg.InputText("",font = (u.fuente), pad =((2,2),(0,15)), size = (36,1), key = "-USERNAME-")],
        u.texts("Contraseña *",17),
        [sg.InputText("",font = (u.fuente), pad =((2,2),(0,15)), size = (36,1), password_char="*", key = "-PASSW-")],
        u.texts("Repetir Contraseña",17),
        [sg.InputText("",font = (u.fuente), pad =((2,2),(0,15)), size = (36,1), password_char="*", key = "-REP_PASSW-")],
        u.texts("Género",17) + [sg.Combo(["Femenino", "Masculino", "No binarie"],default_value = "No binarie",font = (u.fuente), size = (10,1),readonly = True, pad = ((10,30),(0,0)), key = "-GENERO-")] +  
        u.texts("Edad",17) + [sg.Spin([i for i in range(1,120)], initial_value=0, font = (u.fuente),readonly = True, size = (3,1), key = "-EDAD-")],
    ]

    l_cont = [
        u.texts("Registrarse",25,pad = ((100,100),(20,16))),
        [sg.Column(l_cont_form, background_color= u.fondo_color_cont, element_justification="l", pad=(0,0))],
        u.buttons("REGISTRARSE",17,"-REGISTRARSE-",pad =((0,0),(19,9))),
        u.buttons("VOLVER",0,"-VOLVER-",pad =((0,0),(0,20))),
    ]

    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color= u.texto_color,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))
