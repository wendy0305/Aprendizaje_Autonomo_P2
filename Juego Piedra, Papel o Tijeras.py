#Importa el módulo random para generar elecciones aleatorias de la computadora.
import random 
lista=["Piedra", "Papel", "Tijera"]
print("Bienvenidos al juego de Piedra, Papel o Tijeras")

#Inicia un bucle infinito que mantendrá el juego en ejecución hasta que el usuario decida salir.
while True:
    print("Opciones a elegir:")
    print("(1)Piedra")
    print("(2)Papel")
    print("(3)Tijera")
    print("(4)Salir del juego")

#	Intenta convertir la entrada del usuario a un número entero. 
# Si falla <porque el usuario ingresó texto>, muestra un mensaje de error y vuelve al inicio del bucle.

    try:
        jugador=int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, Ingrese un número válido")
        continue
    if jugador==4:
        print("Fin del juego, gracias por partipar.¡Adiós!")
        break
    if jugador not in [1 , 2 ,3]:
        print("La opción seleccionada es invalida, por favor escoge una opción válida")
        continue

#	Convierte la opción numérica del jugador (1-3) en la cadena correspondiente ("Piedra", "Papel" o "Tijera")
    jugador_opcion=lista[jugador-1]

#	La computadora elige aleatoriamente una de las tres opciones.
    computador_opcion=random.choice(lista)
    print("Opción del jugador: ", jugador_opcion)
    print("Opción del computador: ", computador_opcion)

#	Si ambas elecciones son iguales, declara un empate.   
    if jugador_opcion==computador_opcion:
        print("La partida es Empate!")

#	Verifica las combinaciones ganadoras donde el jugador vence a la computadora.
    elif (jugador_opcion=="Piedra" and computador_opcion=="Tijera") or \
         (jugador_opcion=="Papel" and computador_opcion=="Piedra") or \
         (jugador_opcion=="Tijera" and computador_opcion=="Papel"):
        print("¡Ganaste la partida!")
    else:
        print("¡Perdiste la partida!")

#	Pregunta al jugador si quiere continuar, validando que la respuesta sea "si" o "no".
    while True:     
        seguir=input("¿Quieres seguir jugando? (si/no): ").strip() .lower()
        if seguir in ["si", "no"]:
            break
        else:
            print("Por favor, ingrese 'si' paara seguir jugando o 'no' para terminar el juego")

#	Si el jugador no quiere continuar ("no"), muestra un mensaje de despedida y termina el juego.
    if seguir!='si':
        print("Fin del juego, gracias por partipar.¡Adiós!")
        break