

"""
# Manejo de textos y listas
mensaje = "bienvenido al curso de python"
#comidas = ["tacos", "pizza", "hamburguesa"]
comidas = ["ceviche", "pollo a la brasa", "anticucho"]

# Mostrar datos
#print(mensaje)
# Ejemplo de modificación:
print(mensaje.upper())
#print(comidas[0])
print(comidas[1])



Análisis inicial:
1. Ejecuta el código. ¿Cómo se muestra el texto de la variable mensaje en la consola?
#bienvenido al curso de python
2. Observa la instrucción print(comidas[0]). ¿Qué comida se imprimió en pantalla y en qué posición de la lista se encuentra?
#tacos
3. Ejecuta el programa modificado. ¿Qué cambio ocurrió en la salida del texto respecto al código original?
#el texto se muestra en mayusculas
4. Cambia el índice dentro del corchete comidas[0] para mostrar en pantalla la segunda comida de tu lista. ¿Qué número de índice tuviste que utilizar y por qué?
#puse el #1, porque comienza desde 0, por ende pongo 1 porque seria la segunda opcion
5. Modifica la lista comidas para que incluya tres de tus alimentos favoritos reales y vuelve a imprimir únicamente la segunda opción.

BIENVENIDO AL CURSO DE PYTHON
pollo a la brasa

Observa las opciones y complete las definiciones. Métodos disponibles: insert, append, remove, pop y clear.

6. ¿Qué método elimina todos los elementos de la lista? RESPUESTA: clear

7. ¿Qué método elimina un elemento de la lista por su valor de índice? RESPUESTA: pop

8. ¿Qué método elimina un elemento de la lista usando el valor del elemento? RESPUESTA: remove

9. ¿Qué método agrega un elemento al final de la lista? RESPUESTA: append

10. ¿Qué método agrega un elemento en una ubicación específica? RESPUESTA: insert




DESAFÍO DE CÓDIGO 1:

Python


playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:
playerNames.remove("Adam")

# 2. Elimine el primer número de la lista (5) usando 'pop':
playerNumbers.pop(0)

# 3. Use 'append' para agregar estas variables a sus listas:
name = "Lucas" 
num = 7
playerNames.append(name)
playerNumbers.append(num)

# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:
playerNames.insert(0, "Raven")
playerNumbers.insert(0, 1)




Contadores e Iteradores (Counters and Iterators)
Analiza la siguiente función que genera datos para los ejercicios:

Python



import random

def Generate_Numbers():
    numbers = []
    for i in range(20):
        num = random.randint(1, 50)
        numbers.append(num)
    return numbers

# Llamada a la función
mis_numeros = Generate_Numbers()


¿Qué tipo de datos se está agregando a la lista numbers? RESPUESTA: enteros

¿Cuántos números se están agregando exactamente a la lista? RESPUESTA: 20

¿Qué devuelve (return) la función al final de su ejecución? RESPUESTA: la lista numbers



DESAFÍO DE CÓDIGO 2:

Completa las funciones de análisis de datos:

Python

def Even_Numbers(lista_origen):
    even = []
    # TODO: Itere la lista_origen y agregue a 'even' solo los números pares
    return even 

def Ten_Or_Less(lista_origen):
    # TODO: Cree una lista vacía, busque valores <= 10 y devuélvala
    result = []
    for num in lista_origen:
        if num <= 10:
            result.append(num)
    return result

def Calcular_Diferencias(lista_origen):
    # TODO: Calcule la distancia entre números consecutivos
    # Ejemplo: [10, 7, 15] -> [3, 8]
    differences = []
    for i in range(1, len(lista_origen)):
        differences.append(abs(lista_origen[i] - lista_origen[i-1]))
    return differences

    

    Listas 2D (2D Lists)
DESAFÍO DE CÓDIGO 3:

Observa la siguiente matriz 2D que representa un tablero de Tic-Tac-Toe:

Python



tictactoe = [
    ["X", "X", "X"],
    ["-", "O", "-"],
    ["O", "-", "-"]
]


# Escriba el 'if' para detectar si la fila superior (índice 0) tiene tres "X":
# Pista: Debe revisar las posiciones [0][0], [0][1] y [0][2]
if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
    print("La fila superior tiene tres X")
else:
    print("La fila superior no tiene tres X")


14. ¿Qué valor devolvería la instrucción tictactoe[1][1] en el tablero anterior? RESPUESTA: O

15. ¿Para qué sirve un print() vacío que se coloca al final de un bucle que imprime una matriz? RESPUESTA: Para agregar una linea en blanco entre las filas impresas
"""