# ==========================================
# EJERCICIO 2: 
# NOMBRE: Tito
# TAREA 1: Datos de Entrada
# ==========================================
# TODO: Usa la función input() para pedirle al usuario dos números enteros.
#
# Requisitos:
# - Recuerda convertir las entradas a números enteros usando int().
# - Guarda cada valor en una variable diferente (por ejemplo: numero1 y numero2).
#
# Prueba inicial:
# - Ingresa los valores 3 y 8 en la terminal cuando el programa los solicite.
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

# ==========================================
# TAREA 2: 
# ==========================================
# TODO: Declara una nueva variable para guardar el resultado de la suma
# de los dos números ingresados en la Tarea 1.

suma = numero1 + numero2
#print(f"La suma es: {suma}")

# ==========================================
# TAREA 3: Salida con f-strings
# ==========================================
# TODO: Imprime un mensaje final en pantalla combinando los valores 
# de las Tareas 1 y 2.
#
# Requisitos:
# - Utiliza un f-string para formatear el texto.
#
# Salida esperada (si ingresas 3 y 8):
#   La suma de 3 y 8 es: 11

print(f"La suma de {numero1} y {numero2} es: {suma}")

# ==========================================
# TAREA 4:
# ==========================================
# TODO: Abre tu terminal (asegurate de estar dentro de la carpeta adecuada)
# en Windows teclea: python test_codigo2.py
# en Mac/Linux teclea: python3 test_codigo.py
# Debe aparecer ✅ Prueba pasada con éxito para la suma de dos números. 
# Si no, revisa tu codigo de nuevo y repite los pasos.
# Si ocupas mas ayuda agrega tu caso al foro de la clase.

