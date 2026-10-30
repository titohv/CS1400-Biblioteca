"""
====================================================================
Proyecto: Dibujar una pizza con Python Turtle
====================================================================
En este ejercicio aprenderás el PODER DE LAS FUNCIONES:
1. Reutilización: Escribe el código una vez y úsalo muchas veces.
2. Modularidad: Rompe un problema grande (una tarta) en problemas 
   pequeños (porciones/triángulos).
3. Parámetros: Cambia el comportamiento de tu dibujo pasando 
   diferentes argumentos (tamaño, número de rebanadas, color).
====================================================================

import math
import turtle

# ==================================================================
# 1. Configuración Inicial del Entorno
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightcyan")
pantalla.title("El Poder de las Funciones: Tarta de Triángulos")

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)


# ==================================================================
# 2. Definición de Funciones
# ==================================================================

# TODO 1: Completa la definición de la función 'dibujar_triangulo'
def dibujar_triangulo(t, longitud, angulo, color_relleno="orange"):
  
    Dibuja una porción de tarta (triángulo isósceles) usando la tortuga 't'.
    
    Parámetros:
    - t: El objeto Turtle que dibuja.
    - longitud: La longitud de los dos lados iguales (el radio de la tarta).
    - angulo: El ángulo en el vértice central (en grados).
    - color_relleno: El color con el que se pintará la porción.
    
    
    # --------------------------------------------------------------
    # Paso A: Cálculos Matemáticos (Geometría del Triángulo)
    # --------------------------------------------------------------
    
    # 1. Convertimos la mitad del ángulo a radianes para usar trigonometría
    
    
    # TODO 2: Calcula la longitud de la base del triángulo isósceles.
    # FÓRMULA: base = 2 * longitud * sin(angulo / 2)
    
    
    # TODO 3: Calcula el ángulo de giro exterior para la tortuga en las esquinas.
    # Pista: La suma de ángulos internos de un triángulo es 180°.
    # El ángulo en la base es: (180 - angulo) / 2.
    # El giro exterior es: 180 - ángulo_base  =>  90 + (angulo / 2)
    

    # --------------------------------------------------------------
    # Paso B: Dibujo del Triángulo Isósceles
    # --------------------------------------------------------------
    t.color("darkred", color_relleno)
    t.begin_fill()
    
    # TODO 4: Escribe el trazado del triángulo con 'forward' y 'left'.
    # 1. Avanza 'longitud' (Lado 1)
    # 2. Gira 'angulo_giro_base' hacia la izquierda
    # 3. Avanza 'base' (La corteza de la tarta)
    # 4. Gira 'angulo_giro_base' hacia la izquierda
    # 5. Avanza 'longitud' (Lado 2 para regresar al centro)
    # 6. Gira 180° para quedar orientado en dirección opuesta
    
    t.forward(longitud)
    # tu codigo faltante aqui
    t.left(180)  # Reorientar hacia afuera para la siguiente porción
    
    t.end_fill()


# TODO 5: Función que reutiliza 'dibujar_triangulo' para construir la tarta completa. 
# Parametros incluyen porciones, longitud, y el color del relleno.

   
    Dibuja una tarta completa de 'n_porciones' llamando repetidamente
    a la función 'dibujar_triangulo'.
   
    
    # TODO 6: Calcula el ángulo central de cada porción (360° / n_porciones)

    
    # TODO 7: Usa un bucle 'for' para dibujar todas las porciones llamando la funcion dibujar_triangulo


# TODO 8 (EXTRA/OPCIONAL): Función auxiliar para mover la tortuga sin dejar rastro
# def mover_tortuga(t, x, y):
   Mueve la tortuga a las coordenadas (x, y) sin dibujar.
    # Investigar .penup .goto y .pendown


# ==================================================================
# 3. Demostración del Poder de las Funciones
# ==================================================================
# ¡Mira qué fácil es dibujar varias tartas completas en diferentes 
# posiciones, con distintos números de porciones, tamaños y colores!
# TODO 9: aqui deben ir tus instrucciones para dibujar.

# --- Tarta 1: Tarta clásica de 6 porciones ---

# --- Tarta 2: Tarta grande de 12 porciones ---

# --- Tarta 3: Tarta pequeña (o pizza) de 4 porciones ---

# TODO 10: Finalizar ejecución al hacer clic
"""



import math
import turtle

# ==========================================
# 1. Configuración inicial
# ==========================================

pantalla = turtle.Screen()
pantalla.setup(width=900, height=650)
pantalla.bgcolor("lightcyan")
pantalla.title("El Poder de las Funciones: Tarta de Triángulos")

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)


# ==========================================
# 2. Definición de funciones
# ==========================================

# TODO 1: Crear función para dibujar triángulos
# TODO 1: Definir la función
def dibujar_triangulo(t, longitud, angulo, color_relleno="orange"):
    """
    Dibuja una porción de pizza.

    Parámetros:
    t: Tortuga que realiza el dibujo.
    longitud: Tamaño de los lados iguales.
    angulo: Ángulo central de la porción.
    color_relleno: Color de la porción.
    """

    # TODO 2: Calcular la base
    angulo_radianes = math.radians(angulo / 2)
    base = 2 * longitud * math.sin(angulo_radianes)

    # TODO 3: Calcular el ángulo de giro
    angulo_giro_base = 90 + (angulo / 2)

    # TODO 4: Dibujar el triángulo
    t.color("darkred", color_relleno)
    t.begin_fill()

    t.forward(longitud)
    t.left(angulo_giro_base)
    t.forward(base)
    t.left(angulo_giro_base)
    t.forward(longitud)
    t.left(180)

    t.end_fill()


# TODO 5: Función para dibujar la pizza completa
def dibujar_tarta(t, n_porciones, longitud, color_relleno="orange"):

    # TODO 6: Calcular ángulo por porción
    angulo = 360 / n_porciones

    # TODO 7: Repetir según cantidad de porciones
    for i in range(n_porciones):
        dibujar_triangulo(t, longitud, angulo, color_relleno)
        t.right(angulo)


# TODO 8: Mover la tortuga sin dibujar
def mover_tortuga(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ==========================================
# 3. Dibujar las pizzas
# ==========================================

# TODO 9: Dibujar tres pizzas

# Pizza 1: 6 porciones
mover_tortuga(t, -200, 100)
dibujar_tarta(t, 6, 100, "orange")

# Pizza 2: 12 porciones
mover_tortuga(t, 180, 100)
dibujar_tarta(t, 12, 130, "gold")

# Pizza 3: 4 porciones
mover_tortuga(t, 0, -170)
dibujar_tarta(t, 4, 80, "tomato")

# Ocultar la tortuga cuando termine
t.hideturtle()

# TODO 10: Finalizar al hacer clic
pantalla.exitonclick()
