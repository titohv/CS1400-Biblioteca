# ==========================================
# PRÁCTICA DE PYTHON: TIPOS DE DATOS Y OPERADORES
# ==========================================

# TODO 1: Declara un número entero muy grande llamado 'num_grande'
# (Pista: puedes usar guiones bajos como 1_000_000 para facilitar su lectura)
num_grande = 1_000_0

# TODO 2: Declara un número decimal (float) llamado 'num_float'
num_float = 1.147

# Declarando un número entero base
num = 47
num2 = 31

# TODO 3: Escribe 6 problemas matemáticos en variables separadas usando 'num' y cualquier otro número.
# Debes usar los siguientes operadores en cada uno:
# 1. Suma (+)
# 2. Resta (-)
# 3. Multiplicación (*)
# 4. Potenciación (**)
# 5. División exacta (/)
# 6. División entera (//)
suma = num + 369
resta = num - 963
multiplicacion = num * 789
potencia = num ** 20
division_exacta = num / 741
division_entera = num // 123


# ==========================================
# IMPRESIÓN DE RESULTADOS
# ==========================================

# Mostrar los valores guardados en las variables
print("--- VALORES DE LAS VARIABLES ---")
print("Entero corto:", num)
print("Entero grande:", num_grande)
print("Decimal:", num_float)

# Saludo al usuario
saludo = "¡Hola, bienvenido a Python!"
print(saludo)

print("\n--- RESULTADOS MATEMÁTICOS ---")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("Potencia:", potencia)
print("División exacta:", division_exacta)
print("División entera:", division_entera)

print("\n--- TIPOS DE DATOS ---")
print(type(num))
print(type(num_grande))
print(type(num_float))
print(type(saludo))