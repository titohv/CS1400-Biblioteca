"""
Pseudocódigo: Simulación de DigiPet

Estudiante: Tito Huerta
Propósito: Crear una mascota virtual que tenga felicidad, comida y salud. El jugador debe cuidarla para que siga viva


Plan del programa

1.	Iniciar el programa y solicitar el nombre de la mascota
2.	Crear un objeto de la clase DigiPet con felicidad = 100, hambre = 100 (reserva de comida), salud = 100 y edad = 0
3.	Mientras la mascota siga viva, mostrar sus niveles actuales y un menú con las opciones: jugar, alimentar, pasear, acariciar o salir
4.	Leer la opción elegida. Si elige salir, despedirse y terminar el programa
5.	Si elige jugar, subir la felicidad y gastar un poco de comida
6.	Si elige alimentar, aumentar la reserva de comida sin superar 100
7.	Si elige pasear, subir la felicidad y la salud, pero gastar comida
8.	Si elige acariciar, aumentar la felicidad
9.	Si escribe una opción inválida, mostrar un aviso y volver al menú sin avanzar el tiempo
10.	Después de una acción válida, avanzar un día: aumentar la edad y disminuir felicidad, comida y salud
11.	Comprobar si algún nivel es cero o menor. Si es así, informar la causa de la muerte y terminar el juego
12.	Si los tres niveles siguen por encima de cero, repetir el menú

Relación con programación orientada a objetos
La clase DigiPet funciona como un modelo para crear mascotas sus atributos guardan el estado de cada mascota y sus métodos definen las acciones que puede realizar cada objeto mantiene sus propios valores

Reglas importantes
Los valores positivos indican que la mascota sigue viva el atributo hambre se utiliza como reserva de comida: 100 significa que está llena y 0 que se quedó sin alimento los niveles que aumentan no pueden superar 100
"""