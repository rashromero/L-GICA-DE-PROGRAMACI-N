LÓGICA DE PROGRAMACIÓN 
PROYECTO INTEGRADOR 
Génesis Rashell Romero Morales 
17 de Diciembre, 2025
OBJETIVO: Implementar los principios básicos de la lógica de programación para diseñar y desarrollar un programa funcional en el lenguaje Python.
Introducción al proyecto: 
Este proyecto desarrolla un programa en Python basado en el juego piedra, papel o tijera, aplicando los conceptos fundamentales de la lógica de programación. Para su implementación se utilizaron variables, tuplas, listas, bucles y operadores. Antes del desarrollo del programa, se emplearon diagramas de casos de uso, diagramas de flujo y diagramas de arquitectura de datos, lo que permitió comprender la lógica del sistema y estructurar adecuadamente la solución. Además, se investigó, de manera independiente, e implementó otras funciones que complementaron el desarrollo del proyecto. Es así que este enfoque permitió estructurar un programa de manera ordenada y progresiva, con el fin de reducir errores y, que se cumpla con el objetivo del juego. 
FUNCIONALIDAD: 
El programa implementa el juego piedra, papel o tijera en Python.
Al iniciar, el sistema da la bienvenida, solicita el nombre del jugador y verifica si conoce las reglas del juego. En caso negativo, se presenta una explicación breve antes de comenzar, asegurando que todos los usuarios comprendan la dinámica.
Durante el juego:
El usuario ingresa su elección (piedra, papel o tijera).
La computadora selecciona una opción de forma aleatoria mediante el módulo random.
La entrada del usuario se normaliza usando .lower() y .strip() para evitar errores por mayúsculas o espacios.
Se valida que la opción ingresada sea correcta; si no lo es, el sistema solicita nuevamente la elección.
Se comparan ambas elecciones y se determina el resultado: empate, victoria del jugador o victoria de la máquina.
Finalmente, el programa pregunta si el jugador desea continuar jugando. Según su respuesta, el ciclo se repite o el juego finaliza mostrando un mensaje de despedida.
