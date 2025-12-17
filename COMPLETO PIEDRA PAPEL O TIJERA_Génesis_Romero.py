import random
print ("Bienvenido/a al juego de piedra, papel o tijera ☺️") #Bienvenida
Jugador1= input("Ingresa tu nombre 📝:") #Ingreso del nombre del usuario
conocimiento_del_juego= input(f"{Jugador1}, ¿Conoces de que trata el juego 🤔? (si/no)").lower().strip() #Asegurarse de que se conozcan las reglas
if conocimiento_del_juego in ["sí","si"]:
    print (f"Perfecto, {Jugador1} , competirás contra la máquina y serás el primero en iniciar 🤩") #Instrucción que da inicio al juego, si las reglas se conocen
else:
    print (f"{Jugador1}, no te preocupes, estoy aquí para explicarte ☺️") #Explicación juego y reglas, si no hay conocimiento 
    Explicación_y_reglas= ("El juego piedra, papel o tijera es un juego de dos participantes 🧑‍🤝‍🧑", "Tú jugarás contra la máquina 🖥️", "Cada jugador elige al mismo tiempo una de tres opciones: piedra, papel o tijera ✊", "Las reglas son simples:", "Piedra gana a tijera (la rompe) 🪨🥇", "Tijera gana a papel (lo corta) ✂️🥇", "Papel gana a piedra (la envuelve) 📄🥇", "Si ambos jugadores eligen la misma opción, el resultado es empate 🤝") 
    for i in Explicación_y_reglas:
        print (i)
    print (f"Perfecto,{Jugador1} ,ahora que conoces la reglas, vamos a empezar! 🎉") #Inicio al juego, una vez exlicadas las reglas
#Definición de las opciones 
opciones= ("piedra", "papel", "tijera")
Jugando= True
while Jugando: #Continuar jugando repetidas veces
    RespuestaJugador1= input("Escoge una opción (piedra, papel o tijera): ").lower().strip()
    RespuestaJugador2= random.choice (opciones) #La máquina seleccionará una opción al azar
    while RespuestaJugador1 not in opciones: #Asegurar que el Jugador 1 solo use las opciones disponibles
        print ("Opción inválida! Revisa que la opción que escogiste se encuentre dentro de las opciones aceptadas") #Recordar el uso exclusivo de las opciones aceptadas
        RespuestaJugador1= input("Escoge una opción (piedra, papel o tijera): ").lower().strip() #Se repite el mensaje hasta que se escoga una opción aceptada
    print (f"{Jugador1}: {RespuestaJugador1} ") #Se muestra respuesta escogida por el usuario
    print (f"Computador: {RespuestaJugador2}") #Se muestra respuesta aleatoria del computador 
    if RespuestaJugador1 == RespuestaJugador2: #Mismas respuestas
        print ("Es un empate! 🤝")
    elif RespuestaJugador1 == "piedra" and RespuestaJugador2 == "tijera": #Piedra le gana a tijera
        print ("Tú ganas!, Bien hecho! 🎉 ")
    elif RespuestaJugador1 == "papel" and RespuestaJugador2 == "piedra": #Papel le gana a piedra
        print ("Tú ganas!, Bien hecho! 🎉 ")
    elif RespuestaJugador1 == "tijera" and RespuestaJugador2 == "papel": #Tijera le gana a papel
        print ("Tú ganas!, Bien hecho! 🎉 ")
    else: #Si no ocurre o se cumple nada de lo anterior, pierde
        print ("Lamentablemente perdiste. Pero, te tengo una buena noticia: siempre puedes volver a intentar! 🥳")  
    seguir_jugando= input(f"{Jugador1}, ¿Deseas seguir jugando? 🤨, (colocar si o no):").strip().lower() #El jugador decide si desea continuar jugando
    if seguir_jugando in ["sí","si"]: 
        Jugando= True
        print (f"Perfecto, {Jugador1}, seguiremos jugando! 🤓") #Se continúa el juego
    else:
        Jugando= False
        print (f"Okay, {Jugador1}, paramos. Espero volver a verte pronto! 😉") #Se acaba el juego
    
    
    



