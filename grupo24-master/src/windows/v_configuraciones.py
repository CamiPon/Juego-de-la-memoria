import PySimpleGUI as sg
from ..handlers import Utilidades as u


def build(config):

    pad_t = ((10,0),(0,25))
    pad_i = ((10,0),(0,15))


    lvl1 = (["4x2","4x3"],["3x4","3x5"])
    lvl2 = (["4x4","6x2"],["3x6","3x7"])
    lvl3 = (["6x3","6x4"],["6x5","6x6"])

    general = [
        u.texts("Estilos",15, pad = ((10,0),(25,25))) + [sg.Combo(["t1", "t2", "t3", "t4"],default_value = config["estilo"],font = (u.fuente),readonly = True, size = (8,1),key = "-ESTILO-", pad = ((10,0),(25,15)) )],
        u.texts("Tipo de casillas",15, pad = pad_t) + [sg.Combo(["Palabras", "Imagenes"],default_value = config["tipo_elementos"],font = (u.fuente),readonly = True,key = "-ELEMENTOS-", pad = pad_i )],
        [sg.Checkbox("Ayuda", config["ayudas"][0], font = (u.fuente,15), background_color=u.fondo_color_cont, pad = pad_i, enable_events=True, key = "-AYUDAS-" )] + 
        [sg.Spin([i for i in range(0,8)], initial_value= config["ayudas"][1], font = (u.fuente), size = (3,1),readonly = True, key = "-AYUDAS_CANT-",pad = pad_i, visible= config["ayudas"][0])],
        ]

    juego = [
        u.texts("Tiempo máximo",15, pad = ((10,0),(25,25))) + [sg.Spin([i for i in range(40,240)], initial_value= config["tiempo"], font = (u.fuente), readonly= True, size = (3,1), key = "-TIEMPO-",pad = ((10,0),(25,15)))],
        
        u.texts("Cantidad de coincidencias",15, pad = pad_t),
        [sg.Radio("2", "coincidencias",font = (u.fuente,15), default = True if config["coincidencias"] == 2 else False, background_color=u.fondo_color_cont, pad = pad_i, enable_events=True, key="-coinc2-")] +
        [sg.Radio("3", "coincidencias",font = (u.fuente,15), default = True if config["coincidencias"] == 3 else False, background_color=u.fondo_color_cont, pad = pad_i, enable_events=True, key="-coinc3-")],
        
        u.texts("Dimensiones del tablero",15, pad = pad_t),
        u.texts("Nivel 1",15, pad = pad_t) +
        [sg.Combo(lvl1[0] if config["coincidencias"] == 2 else lvl1[1], default_value = config["cant_casillas"]["NIVEL_1"],font = (u.fuente),readonly = True, size = (8,1),key = "-CASILLAS_1-", pad = pad_t)],

        u.texts("Nivel 2",15, pad = pad_t) +
        [sg.Combo(lvl2[0] if config["coincidencias"] == 2 else lvl2[1], default_value = config["cant_casillas"]["NIVEL_2"],font = (u.fuente),readonly = True, size = (8,1),key = "-CASILLAS_2-", pad = pad_t)],

        u.texts("Nivel 3",15, pad = pad_t) +
        [sg.Combo(lvl3[0] if config["coincidencias"] == 2 else lvl3[1], default_value = config["cant_casillas"]["NIVEL_3"],font = (u.fuente),readonly = True, size = (8,1),key = "-CASILLAS_3-", pad = pad_t)],

        ]

    textos = [
        [sg.Text("Elige el texto que deseas cambiar", background_color= u.fondo_color_cont, font=(u.fuente, 15),pad = (60,(25,15)) )],
        [sg.Combo(["Comienzo","Gano","Perdio","Quedan 30 segundos"], default_value = "Comienzo", font=(u.fuente),enable_events = True, readonly=True ,pad =((13,10),(10,20)), key = "-TEXTOS-")],
        [sg.Text("Máximo 50 caracteres", background_color= u.fondo_color_cont, font=(u.fuente, 10),pad = ((13,0),(0,0)) )],
        [sg.InputText("Elije un texto",key="-TXTACTUAL-", font=(u.fuente,15), s=(30,1), pad = ((13,0),(0,15)))],
        u.buttons("APLICAR",14,"-APLITEXTOS-", pad =((10,10),(16,10)), size = (25,1)),
        ]

    l_cont = [
        u.texts("Configuraciones",25,pad = (120,(20,16))),
        
        [sg.TabGroup([[
            sg.Tab("   General   ",general, background_color=u.fondo_color_cont,),
            sg.Tab("   Juego   ",juego, background_color=u.fondo_color_cont),
            sg.Tab("   Textos   ",textos, background_color=u.fondo_color_cont)]],
            background_color = u.fondo_color_cont,
            font = (u.fuente,13),
            selected_background_color = u.otro,
            pad = (20,50)
            )],
        u.buttons("GUARDAR",14,"-GUARDAR-", pad =((10,10),(16,10)), size = (25,1)),
        u.buttons("VOLVER",13,"-VOLVER-",pad =((10,10),(0,10)),size = (30,1)), # + u.buttons("RESTABLECER",13,"-RESTABLECER-",pad =((0,10),(0,10)),size = (15,1)),
        ]

    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color= u.texto_color ,background_color= u.fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color= u.fondo_color_cont, element_justification="c", pad=(0,0))]
        ]

    return sg.Window("MemPy", layout,background_color= u.fondo_color, element_justification="c", margins = (20,20))