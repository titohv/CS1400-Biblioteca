
# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

"""esta función muestra un mensaje de bienvenida personalizado para el usuario utilizando su nombre como argumento"""

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable 
# nombre
# 2. ¿Qué le falta al código para ser completamente reutilizable?
# lo que le falta es que se le agregue un return para que pueda ser reutilizable y no solo imprima el mensaje en pantalla


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final
"""esta función calcula el precio final de un producto después de aplicar un descuento"""

def es_par(numero):
    return numero % 2 == 0
"""esta función determina si un número es par"""
# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# la palabra es def
# 4. Escribe los nombres de las dos funciones definidas arriba.
# las funciones son calcular_descuento y es_par
# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# lo que hace es que calcula el precio final con un descuento del 10% ya que es el valor por defecto del parametro porcentaje
# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# lo que hace es que calcula el precio final con un descuento del 20% ya que se le pasa el valor de porcentaje como argumento


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
# define la función mostrar_bienvenida con un parametro nombre que imprime un mensaje de bienvenida con el nombre proporcionado
# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
# ===
# 9. Cambia las funciones para que acepten decimales en el precio.
# usar float(precio) para convertir el precio a decimal y poder aceptar decimales en el precio


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
# null y no devuelve nada porque la función mostrar_bienvenida() no tiene un return
# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# al usar return la funcion devuelve el valor calculado que se guarda en compra_1 y compra_2
# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
"""PS D:\Tito\Weber State\CS1400> & C:\Users\Tito\.local\bin\python3.14.exe "d:/Tito/Weber State/CS1400/Semana6/lego.py"
--- PRUEBA 1: Mostrar Bienvenida ---
¡Hola, Ana! Bienvenido a clase hoy.
¡Hola, Carlos! Bienvenido a clase hoy.

--- PRUEBA 2: Cálculo de Descuentos ---
Precio con descuento por defecto: $90.0
Precio con 20% de descuento: $160.0
¡Hola, Julio! Bienvenido a clase hoy.
None
Traceback (most recent call last):
  File "d:\Tito\Weber State\CS1400\Semana6\lego.py", line 85, in <module>
    print(descuento)
          ^^^^^^^^^
NameError: name 'descuento' is not defined"""
# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# el motivo es que la variable descuento es una variable local de la función calcular_descuento() y no puede ser accedida fuera de ella por eso no es accesible fuera de la funcion
# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# al cambiar return por print la funcion no devuelve ningun valor por lo que 'compra_1' sería None y al intentar sumar None + 5 se generaría un error de tipo
# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# una manera sencilla seria llamar a la funcion de la siguiente manera: calcular_descuento(100, porcentaje=15) donde 100 es el precio y 15 es el porcentaje de descuento que se le asigna mediante su nombre de parametro
# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.

