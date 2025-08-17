#Importa el módulo random para generar elecciones aleatorias de la computadora.

import random
import getpass

lista = ["Piedra", "Papel", "Tijera"]

#Muestra en la pantalla las reglas del juego
def desplegar_reglas():
    print("""
Reglas del juego Piedra, Papel o Tijera:
- Piedra gana a Tijera.
- Tijera gana a Papel.
- Papel gana a Piedra.
- Puede jugar contra la computadora o en modo multijugador.
- En el modo multijugador, las opciones de cada jugador no se muestran al otro.
- Se pueden jugar múltiples partidas y se llevarán estadísticas.
""")

#En esta función se solicita al jugador introducir un número (1, 2 o 3), que represente Piedra, Papel o Tijera.
#Valida que la entrada sea válida.
#Si la entrada no es válida, imprime un mensaje y se pide la entrada nuevamente hasta que sea correcta.
#Devuelve la opción elegida como un número entero.
def opcion_valida_usuario():
    while True:
        try:
            opcion = int(input("Seleccione opción (1-Piedra, 2-Papel, 3-Tijera): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

#En esta función se oculta la opción del jugador en la partida de multijugador
def opcion_valida_oculta(jugador_num):
    while True:
        opcion = getpass.getpass(f"Jugador {jugador_num}, ingrese su opción (1-Piedra, 2-Papel, 3-Tijera): ")
        if opcion in ['1', '2', '3']:
            return int(opcion)
        else:
            print("Opción inválida, intente de nuevo.")

#Esta función recibe las opciones de los jugadores, ademas de camparar las opciones.
def decidir_ganador(op_j1, op_j2):
    if op_j1 == op_j2:
        return "empate"
    elif (op_j1 == 1 and op_j2 == 3) or (op_j1 == 2 and op_j2 == 1) or (op_j1 == 3 and op_j2 == 2):
        return "jugador1"
    else:
        return "jugador2"

#Aqui se solicita el nombre del jugadores, si es multijugador pide el nombre de los dos jugadores
def pedir_nombres(modo_multijugador):
    if modo_multijugador:
        jugador1 = input("Ingrese nombre Jugador 1: ")
        jugador2 = input("Ingrese nombre Jugador 2: ")
    else:
        jugador1 = input("Ingrese nombre su nombre: ")
        jugador2 = "Computadora"
    return jugador1, jugador2

#Se pregunta al jugador principal si quiere establecer el número de partidas.
#si es invalida, se solicita otra vez otra vez o si responde NO vuelve a solitar despues de cada partida.
def pedir_numero_partidas():
    while True:
        respuesta = input("¿Desea definir número de partidas a jugar? (si/no): ").strip().lower()
        if respuesta == "si":
            while True:
                try:
                    n = int(input("Ingrese número de partidas: "))
                    if n > 0:
                        return n
                    else:
                        print("Ingrese un número positivo.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif respuesta == "no":
            return None
        else:
            print("Respuesta inválida. Por favor escriba 'si' o 'no'.")

#esta función realiza el ciclo completo de una partida: recoger opciones, 
#comparar reglas, mostrar el ganador y entregar el resultado.
#si es modo multijugador llama la función opcion_valida_oculta y oculta la entrada
#si es contra la computadora pide ingresar la opcion, ademas de que la computadora elije aleatoriamente
#Y llama a la función de decidir quien gana e imprime el ganador de la partida
def jugar_partida(jugador1, jugador2, modo_multijugador):
    if modo_multijugador:
        op1 = opcion_valida_oculta(1)
        op2 = opcion_valida_oculta(2)
    else:
        op1 = opcion_valida_usuario()
        op2 = random.choice([1, 2, 3])
        print(f"Opción de {jugador2}: {lista[op2-1]}")
    resultado = decidir_ganador(op1, op2)
    if resultado == "empate":
        print("La partida es empate!")
    elif resultado == "jugador1":
        print(f"¡Gana {jugador1}!")
    else:
        print(f"¡Gana {jugador2}!")
    return resultado

#Esta función muestra un resumen y estadisticas de las partidas jugadas, aqui se inicializa un diccionario 
# para contar las el resultado de las partidas, 

def resumen_estadisticas(partidas_resultados, jugador1, jugador2):
    print("\nResumen de partidas:")
    totales = {"jugador1":0, "jugador2":0, "empates":0}
    for i, res in enumerate(partidas_resultados, 1):
        if res == "empate":
            estado = f"Partida {i}: Empate"
            totales["empates"] += 1
        elif res == "jugador1":
            estado = f"Partida {i}: {jugador1} ganó - {jugador2} perdió"
            totales["jugador1"] += 1
        else:
            estado = f"Partida {i}: {jugador2} ganó - {jugador1} perdió"
            totales["jugador2"] += 1
        print(estado)
    print("\nEstadísticas:")
    print(f"{jugador1}: ganó {totales['jugador1']} partidas, perdió {totales['jugador2']} partidas, empató {totales['empates']} partidas")
    print(f"{jugador2}: ganó {totales['jugador2']} partidas, perdió {totales['jugador1']} partidas, empató {totales['empates']} partidas")

#Esta función gestiona las repeticiones de partidas segun la opción del usuario sobre cunatas jugar
#Crea una lista vacia para guardar el resultado de cada partida, en cada partida nueva imprime que partida se esta jugando
#devuelve la lista con todo los resultados de las partids jugadas
def jugar_repetido(jugador1, jugador2, num_partidas, modo_multijugador):
    resultados = []
    partidas_jugadas = 0
    if num_partidas is not None:
        for _ in range(num_partidas):
            print(f"\nPartida {partidas_jugadas+1}")
            res = jugar_partida(jugador1, jugador2, modo_multijugador)
            resultados.append(res)
            partidas_jugadas += 1
        resumen_estadisticas(resultados, jugador1, jugador2)
    else:
        while True:
            print(f"\nPartida {partidas_jugadas+1}")
            res = jugar_partida(jugador1, jugador2, modo_multijugador)
            resultados.append(res)
            partidas_jugadas += 1
            while True:
                continuar = input("¿Desea jugar otra partida? (si/no): ").strip().lower()
                if continuar in ("si", "no"):
                    break
                else:
                    print("Por favor ingrese 'si' o 'no'.")
            if continuar == "no":
                resumen_estadisticas(resultados, jugador1, jugador2)
                break
    return resultados

#Esta funcion presneta el menu secundario que permite al usuario elegir como quiere jugar o ver 
#las estadisticas dentro del juego, ademas de crear una lista vacia para almacenar los resultados de las partidas
# en caso de escojer una opcion no listada, muestra un mensaje indicando que la opcion es invalida y vuelve a pedir
def menu_jugar():
    partidas_resultados = []
    jugador1 = jugador2 = None
    while True:
        print("\nMenú Opciones para Jugar:")
        print("1. Contra la computadora")
        print("2. Multijugador (2 jugadores)")
        print("3. Ver estadísticas de las partidas")
        print("4. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            jugador1, jugador2 = pedir_nombres(modo_multijugador=False)
            print("Modo contra computadora")
            num_partidas = pedir_numero_partidas()
            partidas_resultados = jugar_repetido(jugador1, jugador2, num_partidas, modo_multijugador=False)
            # Al terminar de jugar, el ciclo continua y muestra menú otra vez
        elif opcion == "2":
            jugador1, jugador2 = pedir_nombres(modo_multijugador=True)
            print("Modo multijugador (2 jugadores)")
            num_partidas = pedir_numero_partidas()
            partidas_resultados = jugar_repetido(jugador1, jugador2, num_partidas, modo_multijugador=True)
            # Al terminar, se retorna aquí y ciclo continúa mostrando menú
        elif opcion == "3":
            if partidas_resultados:
                resumen_estadisticas(partidas_resultados, jugador1, jugador2)
            else:
                print("No hay estadísticas recientemente.")
            # Luego vuelve a mostrar menú
        elif opcion == "4":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")


#Esta funcion muestra el mensaje de bienvenida y presenta un el menu principal tantas veces como el usuario dquiera, a menos que decida salir
#en caso escribir una opcion no listada va a mostrar un mensaje de opcion invalida
def menu_principal():
    print("Bienvenidos al juego de Piedra, Papel o Tijera")
    while True:
        print("\nMenú Principal:")
        print("1. Jugar")
        print("2. Reglas del juego")
        print("3. Salir del juego")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_jugar()
        elif opcion == "2":
            desplegar_reglas()
        elif opcion == "3":
            print("Fin del juego, gracias por participar. ¡Adiós!")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")

#Aqui se comprueba que el rchivo se este ejecutando directamente (no importado), 
# si es asi llama a la funcion menu:principal()que inicia la ejecucion 
# del programa mostrando el menu principal y contrlar el flujo del juego
if __name__ == "__main__":
    menu_principal()
