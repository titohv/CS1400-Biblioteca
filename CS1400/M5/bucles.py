# Impresión manual repetitiva

"""



Sección 1: ¿Por qué usar un Bucle? (Repetición Manual vs. Iteración)
Analiza el siguiente código para comprender la necesidad de los bucles.

Código 1:
Python
# Impresión manual repetitiva
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
Análisis:
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
que debes escribir 100 veces la misma linea de código para saludar a cada estudiante lo cual es ineficiente y propenso a errores
# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? Explica por qué.
no porque el código está escrito de manera estatica y no permite cambiar el número de saludos sin modificar el código manualmente



=============================

Sección 2: Bucle while (Iteración Indefinida)
Analiza cómo la estructura condicional if difiere del bucle while.

Código 2:
Python
# Intento de repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")
Análisis:
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? Explica por qué sucede esto usando un if.

Modificación 1A (Cambio a while):
Sustituye la palabra if por la palabra while en el código anterior y ejecútalo de nuevo.

# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
es un bucle va repetir hasta que reciba una respuesta no y recien asi se detendra el proceso
# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
no porque es dinamico y depende de la respuesta del usuario
Modificación 1B (Bucle Infinito):
Comenta la línea respuesta = input(...) que está dentro del bloque while. Ejecuta el programa e introduce "si".

# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?
el programa entra en un bucle infinito porque la condición del while nunca se vuelve falsa
# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.
la combinación de teclas es Ctrl+C y la otra es Ctrl+Z dependiendo del sistema operativo

# Intento de repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")

respuesta = input("¿Deseas repetir el proceso? (si/no): ")

while respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")







=============================


Sección 3: Bucle for y la Función range() (Iteración Definida)
Usamos for cuando queremos iterar sobre un número conocido de repeticiones o sobre una secuencia.

Código 3:
Python
# Ejemplo de range() simple
num = int(input("Introduce un número límite: "))

for i in range(10):
    print("Iteración:", i)
Análisis:
# 8. Ejecuta el programa e ingresa el valor 10. ¿Cuántas veces se imprimió la palabra "Iteración"? ¿Influyó en algo el número ingresado por teclado en este primer intento?
se imprimio 10 veces y no influyo en nada el numero ingresado porque el rango es fijo de 0 a 9
# 9. Observa la salida numéricas de i. ¿Cuál es el valor inicial y cuál es el valor final impreso?
Iteración: 0 y Iteración: 9
Valor inicial:

Valor final:

# 10. ¿Se llegó a imprimir el número 10 en la consola? Explica por qué Python excluye el límite superior en range().
no lo excluye porque el rango es de 0 a 9 y el limite superior es exclusivo por lo que no se imprime el 10
# 11. Cambia range(10) por range(0, 10). ¿Existe alguna diferencia en el resultado obtenido?
no hay diferencia porque el rango inicia en 0 por defecto
Modificación 2A (Rango con Variable Límite):
Cambia la línea del rango para usar la variable num: range(1, num).
# 12. Ejecuta e ingresa 20. ¿El conteo se detuvo en 20 o en 19?
19
# 13. ¿Qué ajuste matemático debes hacer dentro de range() para que la cuenta incluya exactamente el número ingresado por el usuario?
lo que debo hacer es sumar 1 al limite superior para que el rango sea inclusivo y llegue hasta el numero ingresado por el usuario
Respuesta: range(1, _________)
seria range(1, num + 1) para que el conteo llegue hasta el número ingresado por el usuario
Modificación 2B (Uso del Argumento Step / Paso):
Modifica la línea a: range(2, 11, 2).

# 14. Ejecuta el programa. ¿Qué valores se imprimieron y qué función cumple el tercer argumento dentro de range(inicio, fin, paso)?
se imprimieron los valores 2, 4, 6, 8, 10 y el tercer argumento indica el paso o incremento entre cada valor del rango



# Ejemplo de range() simple
num = int(input("Introduce un número límite: "))

for i in range(2, 11, 2):
    print("Iteración:", i)

============================


Sección 4: Iteración sobre Secuencias (Cadenas y Listas)
Un bucle for permite iterar directamente sobre los elementos de una colección sin necesidad de usar contadores manualmente.

Código 4:
Python
# Iteración sobre una cadena de texto
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

# Iteración sobre una lista
frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)
Análisis:
# 15. En el primer bucle for letra in palabra:, ¿qué representa la variable letra en cada paso del bucle?
interaccion con cada caracter de la cadena palabra, en cada iteracion letra toma el valor de cada caracter de la cadena "Python" desde la primera letra hasta la ultima
# 16. En el segundo bucle for fruta in frutas:, contrasta la iteración directa (for fruta in frutas:) con el acceso por índices (for i in range(len(frutas)):). ¿Cuál de las dos opciones resulta más legible para un principiante y por qué?
interacion directa es mas legible porque no requiere el uso de indices y es mas facil de entender para un principiante ya que se puede leer como "para cada fruta en la lista de frutas" en lugar de tener que usar indices para acceder a cada elemento de la lista



# Iteración sobre una cadena de texto
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

# Iteración sobre una lista
frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)

    


    =============================



    Sección 5: Sentencias de Control de Bucles (break y continue)
Podemos alterar el flujo normal de un bucle mediante instrucciones de control.

Código 5:
Python
# Uso de break y continue
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)
Análisis:
# 17. Observa la salida de la Demostración de continue. ¿Qué número falta en la secuencia impresa y por qué ocurrió esto?
el numero 3 falta en la secuencia impresa porque cuando el bucle llega a num == 3, la instrucción continue hace que se salte la impresión de ese número y pase a la siguiente iteración del bucle
# 18. Observa la salida de la Demostración de break. ¿Qué números se imprimieron y qué hace la instrucción break al ejecutarse?
el número 1 y el número 2 se imprimieron. La instrucción break detiene la ejecución del bucle cuando se cumple la condición (num == 3).
# 19. Supón que construyes un bucle while True: para solicitar claves de acceso. ¿Qué sentencia te permitiría salir del bucle una vez que el usuario ingrese la clave correcta?
la sentencia break permite salir del bucle una vez que el usuario ingrese la clave correcta



# Uso de break y continue
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)

    



=============================


Sección 6: Patrones de Acumulación y Conteo
Un patrón común en programación consiste en acumular valores o contar ocurrencias a medida que iteramos.

Código 6:
Python
# Acumulador de suma y contador de coincidencias
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)
Análisis:
# 20. ¿Con qué valor deben inicializarse las variables suma_total y mayores_a_cinco antes de comenzar el bucle? ¿Qué pasaría si las inicializas dentro del bucle?
sucede que si las inicializas dentro del bucle, cada vez que se ejecute el bucle, las variables se reiniciarán a 0 y no se acumularán los valores correctamente. Por eso deben inicializarse fuera del bucle para mantener su valor a lo largo de todas las iteraciones.
# 21. Explica con tus palabras la diferencia entre un acumulador (suma_total += num) y un contador (mayores_a_cinco += 1).
entonces un acumulador es una variable que se utiliza para sumar o acumular valores a lo largo de las iteraciones del bucle, mientras que un contador es una variable que se utiliza para contar la cantidad de veces que ocurre un evento específico (en este caso, cuántos números son mayores a 5).



# Acumulador de suma y contador de coincidencias
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)



=============================

Sección 7: Normalización de Textos con .lower()
Analiza cómo formatear cadenas dentro o fuera de un bucle para realizar comparaciones precisas.

Código 7
Python
sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")
Análisis:
# 22. Observa las variables sujeto1 y sujeto2. ¿Cuál es la diferencia visual entre ambos textos y cuál es el resultado de la comparación inicial?
la mayuscula y minisucla en la primera letra
# 23. Modifica la condición a if sujeto1.lower() == sujeto2.lower():. Ejecuta el código nuevamente. ¿Qué resultado obtienes y qué transformación realiza el método .lower()?
valido el caracter y no valida si es mayuscula o minuscula, el resultado es "Iguales" ya que el metodo .lower() convierte todos los caracteres de la cadena a minusculas para que la comparacion sea insensible a mayusculas y minusculas
# 24. ¿Por qué es útil aplicar .lower() a las respuestas del usuario cuando trabajamos con entradas dentro de un bucle while (por ejemplo, al validar "SI", "Si" o "si")?
basicamente en formularios de registro de informacion aveces los usuarios ingresan respuestas en diferentes formatos de mayusculas y minusculas, por lo que al aplicar .lower() se estandariza la entrada y se evita errores de validacion por diferencias en el uso de mayusculas y minusculas




sujeto1 = "Python"
sujeto2 = "python"

if sujeto1.lower() == sujeto2.lower():
    print("Iguales")
else:
    print("Diferentes")

    """