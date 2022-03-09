import PySimpleGUI as sg

estilos = {
    "t1" : {
        "fuente" : "verdana",
        "texto_color" : "#f3f4ed",
        "fondo_color_cont" : "#536162",
        "fondo_color" : "#424642",
        "boton_color" : ("#f3f4ed", "#c06014"),
        "otro" : "#c06014",
    },
    "t2" : {
        "fuente" : "verdana",
        "texto_color" : "#f5f9ed",
        "fondo_color_cont" : "#0883b6",
        "fondo_color" : "#0d496f",
        "boton_color" : ("#f3f4ed", "#20daab"),
        "otro" : "#20daab",
    },
    "t3" : {
        "fuente" : "verdana",
        "texto_color" : "#f3f4ed",
        "fondo_color_cont" : "#385fb0",
        "fondo_color" : "#0e254c",
        "boton_color" : ("white", "#6fa1fe"),
        "otro" : "#6fa1fe",
    },
    "t4" : {
        "fuente" : "verdana",
        "texto_color" : "#f3f4ed",
        "fondo_color_cont" : "#8d857d",
        "fondo_color" : "#665858",
        "boton_color" : ("#f3f4ed", "#7a7672"),
        "otro" : "#7a7672",
    }
}

fuente = "verdana"
texto_color = "#f3f4ed"
fondo_color_cont = "#536162"
fondo_color = "#424642"
boton_color = ("#f3f4ed", "#c06014")
otro = "#c06014"

def start(t):
    global fuente
    global texto_color
    global fondo_color_cont 
    global fondo_color
    global boton_color
    global otro
    fuente = estilos[t]["fuente"]
    texto_color = estilos[t]["texto_color"]
    fondo_color_cont = estilos[t]["fondo_color_cont"]
    fondo_color = estilos[t]["fondo_color"]
    boton_color = estilos[t]["boton_color"]
    otro = estilos[t]["otro"]

def texts(*args, pad = (0,0)):
    return [sg.Text(args[0], font=(fuente, args[1]), text_color=texto_color, background_color= fondo_color_cont, pad = pad)]

def buttons(*args, key ="", pad = (0,0), size = (0,0)):
    return [sg.Button(args[0], font = (fuente, args[1]), key = args[2], border_width = 1, button_color =boton_color, pad = pad, size = size)]
