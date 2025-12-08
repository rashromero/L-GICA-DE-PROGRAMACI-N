import random

print ("Bienvenido/a al juego de piedra, papel o tijera") #Bienvenida
Jugador1= input("Ingresa tu nombre") #Ingreso del nombre del usuario
print (f"Perfecto, {Jugador1} , competirás contra la máquina y serás el primero en iniciar") #Instrucción que da inicio al juego
#Definición de las opciones 
opciones= ("piedra", "papel", "tijera")
Jugando= True
while True: #Continuar jugando repetidas veces
    RespuestaJugador1= None
    RespuestaJugador2= random.choice (opciones) #La máquina seleccionará una opción al azar
    while RespuestaJugador1 not in opciones: #Asegurar que el Jugador 1 solo use las opciones disponibles
        RespuestaJugador1= input("Escoge una opción (piedra, papel o tijera): ")
    print (f"{Jugador1}: {RespuestaJugador1} ")
    print (f"Computador: {RespuestaJugador2}")
    if RespuestaJugador1 == RespuestaJugador2: #Mismas respuestas
        print ("Es un empate!")
    elif RespuestaJugador1 == "piedra" and RespuestaJugador2 == "tijera": #Piedra le gana a tijera
        print ("Tú ganas!, Bien hecho! :) ")
    elif RespuestaJugador1 == "papel" and RespuestaJugador2 == "piedra": #Papel le gana a piedra
        print ("Tú ganas!, Bien hecho! :) ")
    elif RespuestaJugador1 == "tijera" and RespuestaJugador2 == "papel": #Tijera le gana a papel
        print ("Tú ganas!, Bien hecho! :)")
    else: #Si no ocurre o se cumple nada de lo anterior, pierde
        print ("Lamentablemente perdiste :(") 



