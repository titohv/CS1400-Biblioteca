#===========================================================
# EJERCICIO de condicionales
# Tito Huerta
# Fecha: 2026-09-08
#===========================================================
"""
##############################################
Parte 1: Rangos Numéricos
Este programa debe clasificar al usuario según su edad. Pon atención a los límites de cada rango:

Niño: 0 a 12 años
Adolescente: 13 a 17 años
Adulto: 18 a 64 años
Adulto Mayor: 65 años o más
Llena los espacios vacíos para completar las respuestas:

1. ¿Qué nombre o título le pondrás a este programa?
#programa de identificacion de rangos de edades

edad = int(input("¿Cuántos años tienes? "))

if edad <= 12:
    print("Niño")

# 2. ¿Qué condición debe ir aquí para detectar a un adolescente?
elif edad > 12 and edad <= 18:
    print("Adolescente")

# 3. ¿Qué condición debe ir aquí para detectar a un adulto?
elif edad > 18 and edad <= 64:
    print("Adulto")

else:
    print("Adulto mayor")

# 4. ¿Qué comentarios le puedes agregar a tu código para seguir la secuencia?


##############################################
Parte 2: Condiciones Múltiples y Depuración
Siguiendo los ejemplos de sentencias vistas en clase, convierte las siguientes reglas de puntaje numérico (0-100) a líneas de pseudocódigo de razonamiento. Puedes poner las respuestas en VS Code usando # o """ """.

Puntajes: 90+: A | 80-89: B | 70-79: C | 60-69: D | 0-59: E

Ejemplo para A: "Si la nota es mayor o igual a 90, entonces la nota es A."

5. Escribe la lógica en pseudocódigo para las calificaciones B, C, D y E:

Si... la nota es mayor o igual a 80 y menor o igual a 89 entonces la nota es B
Si... la nota es mayor o igual a 70 y menor o igual a 79 entonces la nota es C
Si... la nota es mayor o igual a 60 y menor o igual a 69 entonces la nota es D
Si... la nota es menor a 60, entonces la nota es E
6. Traduce tu lógica a Python:

_________________________________________________________ _________________________________________________________ _________________________________________________________ _________________________________________________________
RETO: Sección de Debugging (Depuración)
Reto 1: Encuentra los errores sintácticos o lógicos para hacer que el código funcione correctamente. Puedes apoyarte en el depurador (debugger).

# Función para calcular calificación
def calcular_calificacion(puntaje):
    if puntaje >= 60 and puntaje < 70:
        return "A"
    elif puntaje >= 70 and puntaje < 80:
        return "B"
    elif puntaje >= 80 and puntaje < 90:
        return "C"
    elif puntaje >= 90:
        return "D"
    else:
        return "E"

# Llamando la función (hard-coded 85)
# RETO 2: ¿Puedes mejorar la siguiente línea de código?
print(calcular_calificacion(85))


puntaje = int(input("ingrese una nota de 0 a 100: "))

def calcular_calificacion(puntaje):
    if puntaje >= 60 and puntaje < 70:
        return "D"
    #priemra validacion es del rango 60 a 69, aproecho en poner este
    #valor ya que la nota podria 69.99 y seria menos de 70
    elif puntaje >= 70 and puntaje < 80:
        return "C"
    #proximo rango de validacion de numeros entre 70 a 89
    elif puntaje >= 80 and puntaje < 90:
        return "B"
    #proximo rango de validacion de numeros entre 80 a 89
    elif puntaje >= 90:
        return "A"
    #proximo rango de validacion para numeros mayores a 90
    else:
        return "E"
#intente construir lo que ya se tenia propuesto en el ejercicio
#por eso el orden de las condiciones esta de esa manera, entonces
#para seguir el ejemplo y las cosas que estamos aprendiendo
# ponde un comentario para que lo pueda aclarar
# Llamando la función (hard-coded 85)
# RETO 2: ¿Puedes mejorar la siguiente línea de código?
print(calcular_calificacion(puntaje))


###############################################3
Parte 3: Validación de Opciones con un Menú
En esta sección crearemos un menú interactivo donde el usuario elegirá una opción ingresando un número (1, 2 o 3).

# Validación de Opciones
print("1. Pizza \n2. Hamburguesa \n3. Ensalada")

# Variable para guardar lo que ingrese el usuario
opcion = input("Elige una opción (1-3): ")

if opcion == "1":
    print("Has elegido Pizza")
    
# 7. Agrega el código si el usuario elige 2
______________________________________________

# 8. Agrega el código por si elige 3
______________________________________________

else:
    print("⚠️ Opción no válida")
9. Ejecuta tu menú. ¿Qué pasaría si el usuario ingresa un 4 o la letra g?




# Validación de Opciones
print("1. Pizza \n2. Hamburguesa \n3. Ensalada")

# Variable para guardar lo que ingrese el usuario
opcion = input("Elige una opción (1-3): ")

if opcion == "1":
    print("Has elegido Pizza")
    
# 7. Agrega el código si el usuario elige 2
elif opcion == "2":
    print("Has elegido Hamburguesa")

# 8. Agrega el código por si elige 3
elif opcion == "3":
    print("Has elegido Ensalada")

else:
    print ("⚠️ Opción no válida")

    """

    # ejemplo propio
print("1. KIA \n2. CHEVROLET \n3. MAZDA")

opcion = input("Elige una marca de autos (1-3): ")

if opcion == "1":
    print("Has elegido KIA")
    
elif opcion == "2":
    print("Has elegido CHEVROLET")

elif opcion == "3":
    print("Has elegido MAZDA")

else:
    print ("⚠️ Opción no válida")
