import PySimpleGUI as sg
from ..model.configuracion import configuracion
from ..windows import v_inicio
from ..component import c_menu
from ..component import c_registro
from ..model.usuario import usuario


def start():
    window = loop()
    window.close()

def loop():
    window = v_inicio.build()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED,"Exit"):
            break
        
        if event == "-INICIAR_SESION-" :
            user = usuario(values["-USERNAME-"],values["-PASSW-"]) # cargo el user que entra
            user2 = user.existeUsuario()
            if user2:
                if user.password == user2.password:
                    user = user2
                    user.buscarConfig()
                    window.close()
                    c_menu.start(user)
                else:
                    sg.popup("La contraseña es incorrecta")
            else:
                sg.popup("El usuario no existe")

        if event == "-REGISTRARSE-" :
            window.hide()
            c_registro.start()
            window.un_hide()

        if event == "-ENTRAR_INVITADO-" :
            user = usuario("invitado","invitado")
            user.guardarUsuarioJson()
            conf = configuracion()
            user.setConfig(conf) 
            user.guardarConfigJson() # restablece la configuracion
            window.close()
            sg.popup("Al entrar como invitado no se guardaran los puntos \nacumulados ni las configuraciones una vez que cierres sesión.")
            c_menu.start(user)


    return window
