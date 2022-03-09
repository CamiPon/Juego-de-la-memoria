from src.windows import v_game
from src.windows import v_fin_partida
from src.model.ficha import Fichas
from src.handlers import estadisticas as est
import PySimpleGUI as sg 
import time

def start(user):
    nivel = selec_level()
    seguir = True
    while nivel != "" and seguir:
        window, seguir = loop(user, nivel)
        if seguir:
            nivel = selec_level()
        window.close()


def selec_level():
    '''Función correspondiente a la selección de nivel'''
    window = v_game.build_niveles()
    nivel = ""
    while True:
        event, values = window.read()
        if event == "-VOLVER-" or event == sg.WIN_CLOSED:
            break

        if "NIVEL" in event.strip("-").split("_"):
            nivel = event.strip("-")
            break
    window.close()
    return nivel


def finPartida(username,puntos,nivel,puntaje_partida,tiempo_total,coin_encontradas,cant_coincidencias,msj_final,bonus_tiempo,puntos_ayuda):
    seguir = False
    tiempo = '{:02d}:{:02d}'.format((tiempo_total // 100) // 60,(tiempo_total // 100) % 60)
    puntos = puntos - puntaje_partida - bonus_tiempo
    window1 = v_fin_partida.build(username,puntos,nivel,puntaje_partida,tiempo,coin_encontradas,cant_coincidencias,msj_final,bonus_tiempo,puntos_ayuda)
    while True:
        event, _values = window1.read()
        
        if event == "-VOLVER-" or event == sg.WIN_CLOSED:
            break

        if event == "-VOLVER_JUGAR-" or event == sg.WIN_CLOSED:
            seguir = True
            break

    window1.close()
    return seguir


def time_as_int():
    '''Redondeo y pasaje a entero del tiempo'''
    return int(round(time.time()*100))


ficha = Fichas()

def loop(user, nivel):
    
    # valores relacionados a la funcionalidad del juego
    configuracion = user.configActual()
    
    cant_ayudas = configuracion["ayudas"][1]
    total_ayudas = cant_ayudas

    coincidencias = configuracion["coincidencias"]
    dim_x, dim_y = configuracion["cant_casillas"][nivel].split("x")
    cant_elem = int(dim_x) * int(dim_y)
    pares = int(cant_elem / coincidencias)
    encontrados = 0
    dim_x, dim_y = configuracion["cant_casillas"][nivel].split('x')
    total_palabras_adivinar = int(int(dim_x) * int(dim_y) / configuracion["coincidencias"])
    
    # valores relacionados al puntaje

    puntaje_acierto = int(nivel.strip('NIVEL_')) * 10
    puntaje_total = puntaje_acierto * pares + 100
    puntaje_partida = 0
    bonus_tiempo = 0
    puntos_ayuda = 0

    # Inicio del tiempo
    current_time = 0
    start_time = time_as_int()

    coordenadas_coincidencias = [] # coordenadas de todas las coincidencias encontradas
    coordenadas_f_seleccionadas = [] # coordenadas de las fichas actualmente seleccionadas
    fichas_seleccionadas = [] # palabras relacionadas a las fichas seleccionadas

    clic = 0
    resta = 0
    hayNClics = False


    # establecimiento de valores necesarios para registrar (estadísticas)
    datos = est.abrirArchivo()
    partida = 1
    if len(datos) > 1:
        partida = int(datos[len(datos)-1][1]) + 1
    evento = 'inicio_partida'
    estado = ''

    # guardado del registro de inicio de juego
    est.guardarEstadistica(datos,current_time,partida,total_palabras_adivinar, evento, user.username, user.genero, user.edad, estado,nivel)

    # Mensaje del comienzo
    sg.popup(configuracion["textos"]["Comienzo"],auto_close = True, auto_close_duration = 3,)

    window = v_game.build(user,configuracion,nivel,ficha,puntaje_total)

    termino = False
    while True:
        event, _values = window.read(timeout=10)
        current_time = time_as_int() - start_time
        evento = 'intento'

        if event == "-AYUDA-":
            if cant_ayudas != 0:
                inicio = int(round(time.time()*100))
                cant_ayudas = cant_ayudas - 1
                window["-X-"].Update("{} / {}".format(cant_ayudas,total_ayudas))
                puntaje_partida = puntaje_partida - 5
                puntos_ayuda += -5 
                x, y = ficha.ayuda(window,coordenadas_coincidencias,configuracion["tipo_elementos"]) # Da vuelta una ficha al azar
                window.refresh()
                resta = 0
                while resta < 2:
                    resta = int(round(time.time())) - (inicio // 100)
            window[f"cell-{x}-{y}"].Update("                 ",image_filename = ficha.lista[x][y]["dorso"], image_size=(110,110), image_subsample=3,disabled = False)


        if event == "-SALIR-" or event == sg.WIN_CLOSED:
            if sg.popup("Estas seguro que deseas salir?",button_type = 4) == "OK":
                termino = True
                est.guardarEstadistica(datos,current_time,partida,total_palabras_adivinar, 'fin', user.username, user.genero, user.edad, 'abandonada',nivel)
                est.guardarEnArchivo(datos)
                break

        # comprobación de coincidencias
        if hayNClics:
            resta = ((current_time // 100) % 60) - ((start // 100) % 60)
            if resta == 1:
                hayNClics = False
                resta = 0
                if (clic > 1):
                    if fichas_seleccionadas != list(reversed(fichas_seleccionadas)): # Si las fichas que estan dadas vuelta son distintas
                        ficha.mostrarDorso(window, coordenadas_f_seleccionadas)
                        clic = 0
                        estado = 'error'
                        palabra = fichas_seleccionadas[len(fichas_seleccionadas)-1]
                        coordenadas_f_seleccionadas = []
                        fichas_seleccionadas = []
                    elif (clic == configuracion["coincidencias"]): # entra cuando todas las fichas sean iguales y cuando sean la cantidad de coincidencias
                        clic = 0
                        estado = 'ok'
                        palabra = fichas_seleccionadas[len(fichas_seleccionadas)-1]
                        fichas_seleccionadas = []
                        # agrego las coordenadas de las fichas en las que hay coincidencias para que no se puedan volver a seleccionar
                        for coor in coordenadas_f_seleccionadas:
                            coordenadas_coincidencias.append(coor)
                        coordenadas_f_seleccionadas = []
                        puntaje_partida += puntaje_acierto
                        window["-PUNTAJE-"].update(f"Puntos: {puntaje_partida} / {puntaje_total}") # VER no se por que no escribe puntaje_partida
                        encontrados += 1
                        window["-CONJUNTOS-"].update(f"Conjuntos encontrados: {encontrados}/{pares}")
                    est.guardarEstadistica(datos,current_time,partida,total_palabras_adivinar, evento, user.username, user.genero, user.edad, estado,nivel, palabra = palabra)

            else:
                continue

        # selección de una ficha
        if  "cell" in event.split("-"):
            x,y = event.strip("cell-").split("-")
            x,y = int(x), int(y)
            if (x,y) in coordenadas_f_seleccionadas or (x,y) in coordenadas_coincidencias: #con esto se verifica que no se haya pulsado un botón que ya esté presionado
                continue
            else: 
                ficha.mostrarFrente(window,configuracion["tipo_elementos"],x,y)
                coordenadas_f_seleccionadas.append((x,y))
                fichas_seleccionadas.append(ficha.lista[x][y]["palabra"][0])
                clic += 1
                window.refresh()
            if (clic == 1):
                est.guardarEstadistica(datos,current_time,partida,total_palabras_adivinar, evento, user.username, user.genero, user.edad, 'error', nivel, palabra = ficha.lista[x][y]["palabra"][0])
            if (clic == 2 or clic == 3):
                hayNClics = True
                start = current_time

        current_time = time_as_int() - start_time

        if (configuracion["tiempo"] < (current_time // 100)) or (len(coordenadas_coincidencias) == int(dim_x) * int(dim_y)):
            if(configuracion["tiempo"] < (current_time // 100)):
                estado = 'timeout'
                msj_final = configuracion["textos"]["Perdio"]
            else:
                msj_final = configuracion["textos"]["Gano"]
                estado = 'finalizada'
                if((current_time // 100) < configuracion["tiempo"]/2):
                    bonus_tiempo = 100
                elif(configuracion["tiempo"]*0.5 < (current_time // 100) < configuracion["tiempo"]*0.75):
                    bonus_tiempo = 75
                else:
                    bonus_tiempo = 50

            # guardado del registro final del juego
            est.guardarEstadistica(datos,current_time,partida,total_palabras_adivinar, 'fin', user.username, user.genero, user.edad, estado, nivel)
            est.guardarEnArchivo(datos)
            
            # guardado de puntaje total obtenido
            user.puntos[nivel] = user.puntos[nivel] + puntaje_partida + bonus_tiempo
            user.guardarUsuarioJson()

            if sg.popup("Jugar de nuevo?",button_type = 4) == "OK":
                seguir = True
            else:
                seguir = False
            break

        if ((configuracion["tiempo"]*100) - current_time  == 3000): # Mensaje quedan 30 segundos
            window['-30_SEG-'].Update(configuracion["textos"]["Quedan 30 segundos"])

        window['-TIMER-'].Update('{:02d}:{:02d}'.format((current_time // 100) // 60,(current_time // 100) % 60))

    # if termino == False: # Si no presiono el boton salir
    #     seguir = finPartida(user.username,user.puntos[nivel],nivel,puntaje_partida,current_time,encontrados,pares,msj_final,bonus_tiempo,puntos_ayuda)
    # else:
    #     seguir = False

    return window, seguir