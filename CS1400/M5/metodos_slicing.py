# Conteo descendente
"""
num = int(input("Introduce el número inicial: "))

for i in range(num, 0, -1):
    print("Conteo:", i)

    # 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?

Inicio: 10 | Fin: 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
porque de esa forma se detiene el conteo en el numero 1 ya que si fuera positivo el conteo nunca llegaria a 0 y se detendria en el número 1
# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
porque el valor final en range() es exclusivo por lo que al poner 0 el conteo se detiene antes de llegar a 0 terminando en 1
Práctica de Sección:
# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:
Respuesta: range( _______ , _______ , _______ )

num = int(input("Introduce el número inicial: "))
for i in range(num, -1, -2):
    print("Conteo:", i)

===========================
import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F

# 5. ¿Resultado de la Línea A round(decNum, 2)? -34.57

# 6. ¿Resultado de la Línea B round(decNum, 0)? -35.0

# 7. ¿Resultado de la Línea C int(decNum)? -34 (Pista: ¿Redondea o trunca los decimales?)

# 8. ¿Resultado de la Línea D abs(decNum)? 34.5678

# 9. ¿Resultado de la Línea E math.pow(intNum, 2)? 81.0

# 10. ¿Resultado de la Línea F math.sqrt(intNum)? 3.0



===========================


Sección 3: Comparación de Textos mediante ASCII / Unicode
Las funciones max() y min() en Python no solo funcionan con números; en cadenas de texto comparan valores según la tabla de caracteres ASCII/Unicode.

Código 3.1:
Python
miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)
Análisis:
# 11. Antes de ejecutar: ¿Cuál crees que será el resultado devuelto por max()?

Predicción: Zanahoria
# 12. Ejecuta el código. ¿Cuál fue el resultado real devuelto?

Resultado: manzana
 

# 13. Sabiendo que en la tabla ASCII las mayúsculas tienen valores numéricos menores que las minúsculas, explica por qué "manzana" fue seleccionada como la mayor frente a "Zanahoria".
sucede porque la letra "Z" de "Zanahoria" es mayuscula y tiene un valor ASCII menor que la letra "m" de "manzana", que es minuscula por lo tanto al comparar las cadenas "manzana" se considera mayor que "Zanahoria"
# 14. Cambia la función de max() a min(). ¿Qué valor obtienes ahora y por qué?

Resultado: Banano



miMax = min("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)




===========================

Sección 4: Aplicación Práctica – Física y Matemáticas
La policía de tránsito calcula la velocidad v de un auto a partir de la longitud d de la huella de frenado utilizando la fórmula: v = \sqrt{20 \cdot d}.

Código 4.1:
Python
import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = 

print("Velocidad estimada del auto:", round(v, 2), "km/h")
Análisis:
# 15. Completa la asignación v = en el código superior utilizando la función math.sqrt() y la fórmula entregada. Escribe la línea completa a continuación:

Respuesta: v = math.sqrt(20 * d)



import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")







============================



Sección 5: Segmentación de Cadenas (Slicing)
El slicing o rebanado permite extraer subcadenas utilizando la sintaxis cadena[inicio:fin:paso].

Código 5.1:
Python
nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])
Análisis:
# 16. ¿Qué carácter imprime exactamente nombre[0]? imprime la letra "B" que es el primer caracter de la cadena "Building Puentes"

# 17. ¿En qué posición (índice) exacta se encuentra el espacio en blanco entre ambas palabras? en el índice 8 ya que es el noveno caracter de la cadena "Building Puentes"

# 18. Modifica los índices en nombre[X:Y] para extraer e imprimir exactamente la palabra "Puentes".

Opción con 2 valores: nombre[ 8 : 16 ]

Opción con límite implícito: nombre[ 8 : ]
nombre = "Building Puentes"

print("Índice 0:", nombre[8])
print("Segmento:", nombre[8:16])



============================


Sección 6: Filtrado e Inspección de Caracteres en Cadenas
Podemos usar bucles combinados con condicionales para inspeccionar y filtrar tipos específicos de caracteres dentro de un texto.

Código 6.1:
Python
texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)
Análisis:
# 19. Ejecuta el programa e ingresa el texto "3 tigres en 2 árboles". ¿Qué valor imprime contador_numeros? 2

# 20. Observa la condición del if. Explica cómo evalúa Python si un carácter individual es un dígito numérico usando los operadores >= y <=.
muestra que Python compara el valor ASCII de cada caracter ingresado con los valores ASCII de "0" y "9" si el valor del caracter esta entre estos dos valores se considera un digito numerico y se incrementa el contador
texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)




Sección 7: Investigación de Métodos de Cadenas (String Methods)
Investiga en la documentación oficial de Python o en W3Schools el funcionamiento de los siguientes métodos y explica brevemente para qué sirven:

# 21. Método .rfind('a'):

Descripción: hace una busqueda de la ultima aparición del caracter 'a' en la cadena y devuelve el indice de esa posición si no se encuentra devuelve -1

# 22. Método .isalpha():

Descripción: devuelve True si todos los caracteres de la cadena son letras (a-z, A-Z) y la cadena no está vacia de lo contrario devuelve False

# 23. Método .isdigit():

Descripción: devuelve True si todos los caracteres de la cadena son digitos (0-9) y la cadena no esta vacia de lo contrario devuelve False

"""
