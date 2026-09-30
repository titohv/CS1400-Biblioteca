"""
# Nombres de la pareja: Tito
# Programa para determinar el número de dígitos
num = int(input("Ingresa un número: "))

if num < 0:
    print("Número Negativo")
elif num < 10:
    print("Número de un Dégito")
if num < 100:
    print("Número de dos Dégitos")
else:
    print("Número bastante grande")



# Programa de Verificación de Licencia
age = int(input("Ingresa tu edad: "))
test = input("¿Pasaste el examen de conducir? (s/n): ")

if age >= 16 and (test == "s" or test == "S"):
    print("Puedes conducir")

elif age < 16 and (test == "s" or test == "S"):
        print("eres muy joven")

else:
    print("Debes pasar el examen y tener al menos 16 años")

    
    """


# Programa de Labores del Hogar
oficios = int(input("¿Cuántas labores realizaste? "))
monto = oficios * 0.50

cuarto = input("¿Limpiaste tu habitación? (s/n): ")
if cuarto == 's' or cuarto == 'S':
    monto += 1
else:
    monto -= 0.50

tarea = input("¿Terminaste la tarea escolar? (s/n): ")
if tarea == 's' or tarea == 'S':
    monto += 2 
else:
    monto -= 0.50

print("Has ganado total:", monto)