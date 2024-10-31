# BLACKJACK

#### Objetivo del juego:
# 	Conseguir 21 puntos o plantarse con más puntos que el otro jugador.


#### Funcionamiento:
# 	1. Gana el jugador que tenga la puntuación más alta sin pasarse de 21 puntos.
# 	2. La baraja de cartas es la cadena de caracteres "A234567890JKQ". Las cartas tienen los siguientes puntos:
 
# 		A -> 1 o 10 (según le venga mejor al resto de cartas que tiene en su poder el jugador)
# 		2...9 -> el propio valor del número.
# 		0, J, Q, K -> 10
  
# 	3. Cada jugador irá solicitando cartas por turnos, después del primer turno obligatorio, un jugador puede plantarse cuando lo decida.
# 	4. Después de cada turno, se debe mostrar la información de la ronda o turno, las cartas y puntos de cada jugador:
 
# 		RONDA 3
# 		J1 - jugador1 - A3K (14)
# 		J2 - jugador2 - A44 (18)
  
# 	5. Cuando un jugador se pasa de 21, automáticamente pierde y gana el otro jugador.
# 	6. Las cartas de los jugadores y puntuaciones se revelan a la vez después de pasar el turno ambos jugadores, es decir, cada jugador decide pedir una carta más o plantarse y a continuación se muestra la información de cada jugador.
 
#  		RONDA 3
# 		J1 - jugador1 - 63K (19)
# 		J2 - jugador2 - J4Q **se pasa**
  
# 	7. El programa debe solicitar el modo de juego y a continuación el nombre o apodo del o los jugadores.
# 	8. Cada jugador pide una carta por turno o se planta. Como mínimo un jugador debe solicitar una carta, es decir, la primera vez no se le da la opción a plantarse. Pero el resto de turnos si.
# 	9. El juego acaba cuando ambos jugadores se plantan. Mientras que un jugador no se pase de 21 puntos y no se plante se debe preguntar si quiere una carta más.
# 	10. Cuando finaliza el juego se debe mostrar lo siguiente (4 posibilidades):

# 		JUEGO TERMINADO - Ronda 3
# 		Game over ¡Los dos os habéis pasado!
# 		J1 - jugador1 - 4K9 (23)
# 		J2 - jugador2 - J70 (27)

# 		JUEGO TERMINADO - Ronda 3
# 		¡Empate!
# 		J1 - jugador1 - 4K5 (19)
# 		J2 - jugador2 - A9 (19)
    
# 		JUEGO TERMINADO - Ronda 3
# 		¡Gana J1 - jugador1!
# 		J1 - jugador1 - JQA (21)
# 		J2 - jugador2 - 491J (24)

# 		JUEGO TERMINADO - Ronda 3
# 		¡Gana J2 - jugador2!
# 		J1 - jugador1 - 3K5 (18)
# 		J2 - jugador2 - 28Q (20)

import time
import os
import random

VICTORIA = int(21)

def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear' (os.name == "posix").
    """

    try:
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
    except Exception as e:
        mostrar_error(f"Problemas al intentar limpiar la pantalla: {e}")

def pausa(tiempo = 0, tecla_enter = False, limpiar = True):
    """
    Pausa la ejecución del programa según los parámetros especificados.

    Args:
        tiempo (int, opcional): Número de segundos para la pausa. Si es mayor a 0, se pausa 
            por este tiempo y se ignora `tecla_enter`.
        tecla_enter (bool, opcional): Si es True y `tiempo` es 0, espera a que el usuario presione 
            ENTER para continuar.
        limpiar (bool, opcional): Si es True, limpia la pantalla después de la pausa.

    """

    if tiempo > 0:
        time.sleep(tiempo)
    elif tecla_enter and tiempo == 0:
        input("\nPresione ENTER para continuar...")

    if limpiar:
        limpiar_pantalla()

def mostrar_error(msjError: str):
    """Muestra un mensaje de error en la consola y pausa la ejecución.

    Args:
        msjError (str): Mensaje de error que se mostrará al usuario.
    """
    print("\n*ERROR* " + str(msjError) + "\n")
    pausa(2)

def clear():
    os.system("cls")

def comprobar_numero():
    numero = None
    while numero is None:
        try:
            numero = int(input(f"\n-> "))
        except ValueError:
            print("**Entrada inválida**")

    return numero

def pedir_numero():
    numero_correcto = False
    while not numero_correcto:
        print("1. Dos jugadores.\n2. Un jugador contra la máquina.")
        pausa(1, limpiar = False)
        numero = comprobar_numero()
        if numero == 1 or numero == 2:
            numero_correcto = (numero != None)
        else:
            clear()
            mostrar_error("Entrada invalida")
    
    return numero

def valor_carta(carta, puntuacion):
    carta = carta[:1]
    valor = 0 
    if carta == "A":
        if puntuacion <= 10:
            valor = 11
        else:
            valor = 1
    if carta == "2":
        valor = 2
    if carta == "3":
        valor = 3
    if carta == "4":
        valor = 4
    if carta == "5":
        valor = 5
    if carta == "6":
        valor = 6
    if carta == "7":
        valor = 7
    if carta == "8":
        valor = 8
    if carta == "9":
        valor = 9
    if carta == "0" or carta == "J" or carta == "Q" or carta == "K":
        valor = 10

    return valor

def ronda(n_ronda, cartas_j1, cartas_j2, puntuacion_j1, puntuacion_j2, jugador_1, jugador_2, ronda_final = False):

#       RONDA 3
# 		J1 - jugador1 - A3K (14)
# 		J2 - jugador2 - A44 (18)

    if ronda_final:
        ronda = f"JUEGO TERMINADO - Ronda {n_ronda}\n{evaluar_resultado(puntuacion_j1, puntuacion_j2)}\nJ1 - {jugador_1} - {cartas_j1} ({puntuacion_j1})\nJ2 - {jugador_2} - {cartas_j2} ({puntuacion_j2})\n"
    else:
        if puntuacion_j1 > VICTORIA:
            puntuacion_j1 = "*se pasa*"
        if puntuacion_j2 > VICTORIA:
            puntuacion_j2 = "*se pasa*"
        ronda = f"RONDA {n_ronda}\nJ1 - {jugador_1} - {cartas_j1[:-1]} ({puntuacion_j1})\nJ2 - {jugador_2} - {cartas_j2[:-1]} ({puntuacion_j2})\n"

    return ronda

def pedir_seguir(jugador: str) -> bool:
    opcion = None

    while opcion == None:
        time.sleep(0.5)
        opcion = input(f"-> {jugador}, ¿quieres continuar? (S/N): ").lower()
        if opcion != "s" and opcion != "n":
            mostrar_error("Introduzca una opción válida.")
            opcion = None
    
    if opcion == "s":
        return True
    else:
        return False

def comprobar_nick(nick: str) -> bool:
    for caracter in nick:
        if not caracter.isalpha() and not caracter.isdigit() and caracter != " " and caracter != "," and caracter != ".":
            return False

    return True

def pedir_nick(msj) -> str:
    nick = ""
    nick_correcto = False

    while not nick_correcto:
        nick = input(f"{msj} - Introduce tu nick: ")
        if comprobar_nick(nick) == True:
            nick_correcto = True
        else:
            mostrar_error("El nick debe estar formado por palabras y/o números.")

    return nick

def contar_puntuacion(cartas):

    puntuacion = 0
    for carta in cartas:
        puntuacion += valor_carta(carta, puntuacion)
    
    return puntuacion

def blackjack():
    # Variables de inicio de la partida.
    baraja = crear_baraja()
    n_ronda = 1
    cartas_j1 = ""
    cartas_j2 = ""
    puntuacion_j1 = 0
    puntuacion_j2 = 0
    salir = False
    seguir_j1, seguir_j2 = True, True
    modo_de_juego = modo_juego() # 'True' para dos jugadores | 'False' para un solo jugador contra la máquina.
    riesgo_bot = random.randint(0, 6) # Define cuánto se va a arriesgar la máquina cada partida. El bot se conformará con valores aleatorios a una distancia del 0% al 30% del valor de VICTORIA. Si VICTORIA == 21, en algunas ocasiones se plantará con 16, en otras con 21 (y valores intermedios).
    # PREGUNTAR A DIEGO POR QUÉ NO FUNCIONA ESTO: (30 * VICTORIA / 100) // 1
    bot_plantado = False
    clear()

     # Mensaje de presentación del modo de juego elegido.
    if modo_de_juego:
        jugador_1 = pedir_nick("Jugador 1")
        jugador_2 = pedir_nick("Jugador 2")
        clear()
        print("Iniciando partida de dos jugadores...")
    if not modo_de_juego:
        jugador_1 = pedir_nick("Jugador 1")
        jugador_2 = "BOT"
        clear()
        print("Iniciando partida de un jugador contra la máquina...")
    pausa(3)
    clear() # La partida empieza tras una pausa de 3 segundos.

    while not salir:
        if seguir_j1 or n_ronda == 1:
            ultima_carta_j1 = baraja[:2]
            cartas_j1 += ultima_carta_j1 + " "
            baraja = baraja[2:]
            puntuacion_j1 = contar_puntuacion(cartas_j1)
        if seguir_j2 or n_ronda == 1:
            ultima_carta_j2 = baraja[:2]
            cartas_j2 += ultima_carta_j2 + " "
            baraja = baraja[2:]
            puntuacion_j2 = contar_puntuacion(cartas_j2)
        print(ronda(n_ronda, cartas_j1, cartas_j2, puntuacion_j1, puntuacion_j2, jugador_1, jugador_2))
        
        if not seguir_j1 and not seguir_j2 or (puntuacion_j1 > VICTORIA and puntuacion_j2 > VICTORIA) or (not seguir_j1 and puntuacion_j2 > VICTORIA) or (not seguir_j2 and puntuacion_j1 > VICTORIA):
            salir = True
            ronda_final = True
            n_ronda -= 1
        else:
            if seguir_j1:
                if puntuacion_j1 < VICTORIA:
                    seguir_j1 = pedir_seguir(jugador_1)
                else:
                    seguir_j1 = False
            if modo_de_juego:
                if seguir_j2:
                    seguir_j2 = pedir_seguir(jugador_2)
            else:
                seguir_j2 = (VICTORIA - puntuacion_j2) > riesgo_bot
                if not seguir_j2 and not bot_plantado:
                    pausa(2)
                    print("* BOT: Me planto >.< *")
                    pausa(3)
                    bot_plantado = True
                if seguir_j2:
                    pausa(2)
                    print("* BOT: Cojo carta ;) *")
                    pausa(2)
            n_ronda += 1
        clear()
    
    print(ronda(n_ronda, cartas_j1, cartas_j2, puntuacion_j1, puntuacion_j2, jugador_1, jugador_2, ronda_final))

def evaluar_resultado(puntuacion_j1, puntuacion_j2):
    # Posibles resultados de la partida.
    if puntuacion_j1 > VICTORIA and puntuacion_j2 > VICTORIA:
        return "Game over ¡Los dos os habéis pasado!"
    elif puntuacion_j1 == puntuacion_j2:
        return "¡Empate!"
    elif puntuacion_j2 > VICTORIA and puntuacion_j1 <= VICTORIA:
        return "¡Gana J1 - jugador1!"
    elif puntuacion_j1 > VICTORIA and puntuacion_j2 <= VICTORIA:
            return "¡Gana J2 - jugador2!"
    elif puntuacion_j1 < VICTORIA and puntuacion_j2 < VICTORIA:
        if puntuacion_j1 > puntuacion_j2:
            return "¡Gana J1 - jugador1!"
        else:
            return "¡Gana J2 - jugador2!"
    elif puntuacion_j1 == VICTORIA and puntuacion_j2  != VICTORIA:
        return "¡Gana J1 - jugador1!"
    elif puntuacion_j2 == VICTORIA and puntuacion_j1  != VICTORIA:
        return "¡Gana J2 - jugador1!"

def barajar_cartas(baraja_ordenada: str):
    baraja_barajada = ""
   
    while len(baraja_ordenada) > 0:
        # Crea 
        indice_aleatorio = random.randint(0, (len(baraja_ordenada) // 2) - 1) * 2
        carta_aleatoria = baraja_ordenada[indice_aleatorio:indice_aleatorio + 2]
        baraja_barajada += carta_aleatoria
        baraja_ordenada = baraja_ordenada[:indice_aleatorio] + baraja_ordenada[indice_aleatorio + 2:]

    return baraja_barajada

def crear_baraja():
    baraja = "A234567890JQK"
    baraja_ordenada = ""

    for i in baraja:
            baraja_ordenada += i + "\u2665" + i + "\u2666" + i + "\u2663" + i + "\u2660"

    return barajar_cartas(baraja_ordenada)

def modo_juego():

    modo_de_juego = pedir_numero()
    if modo_de_juego == 1:
        return True
    else:
        return False

def main():
    clear()
    blackjack()
    # baraja = "A234567890JQK" * 4
    # palos "\u2665 \u2666 \u2663 \u2660"

if __name__ == "__main__":
    main()