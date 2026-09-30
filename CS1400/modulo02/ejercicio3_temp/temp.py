# ==========================================
# EJERCICIO 3: Conversor de Temperatura
# NOMBRE:
# ==========================================

# TODO: Paso 1. Declara una variable para solicitar al usuario 
# la temperatura en grados Celsius. 
#
# Requisitos:
# - Recuerda convertir la entrada a número decimal usando float(), 
#   ya que la temperatura puede incluir decimales.

temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# TODO: Paso 2. Calcula la conversión a grados Fahrenheit.
#
# Fórmula matemática:
#   Fahrenheit = (Celsius * 9/5) + 32

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# TODO: Paso 3. Muestra el resultado final usando print() y un f-string.
#
# Ejemplos de salida esperada:
# - Si el usuario ingresa 0:
#   La temperatura en Fahrenheit es: 32.0
#
# - Si el usuario ingresa 25.7:
#   La temperatura en Fahrenheit es: 78.26  (o 78.3 si se redondea)

print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit}")

# TODO: Paso 4. Evaluación del Clima (Estructura Control: if / else)
# Usa una estructura condicional (if / else) para clasificar la temperatura recibida.
#
# Requisitos:
# - Si la temperatura en grados Celsius es igual o mayor a 30:
#     Imprime: "¡Hace mucho calor! Mantente hidratado."
# - De lo contrario (else):
#     Imprime: "El clima está agradable o fresco."

if temperatura_celsius >= 30:
    print("¡Hace mucho calor! Mantente hidratado.")
else:
    print("El clima está agradable o fresco.")
    