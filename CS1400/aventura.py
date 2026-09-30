# --- PROGRAMA DE PRÁCTICA BOOLEANA ---
# Nombres de la pareja: Tito
# Propósito del programa: decidir si es posible realizar una aventura

# Programa para practicar operadores booleanos (Boolean Operator Practice)

print("planificador de aventuras de fin de semana")
print("vamos a practicar el uso de los operadores and or y not\n")

# obtener entradas del usuario y convertirlas a valores booleanos
# usamos lower para aceptar sí si y yes
tiene_tiempo = input("¿Tienes tiempo libre? (sí/no): ").strip().lower() in ["sí", "si", "yes"]
buen_clima = input("¿Hace buen tiempo? (sí/no): ").strip().lower() in ["sí", "si", "yes"]
tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower() in ["sí", "si", "yes"]
tiene_dinero = input("¿Tienes dinero para gastar? (sí/no): ").strip().lower() in ["sí", "si", "yes"]

print("\n--- Resultados de la Lógica Booleana ---")

# 1. Hay que tomar una decisión de cómo ponerle a esta variable. 
# Sabiendo que con el operador AND (Y): Ambas condiciones deben ser verdaderas (True)
# ¿Qué haces si tienes tiempo y hace buen clima?
# debe mostrar un mensaje si ambas condiciones son verdaderas

#¿Cómo le pondrán a esta variable? Reemplaza variable_1 por algo más descriptivo.
disponibilidad_clima = tiene_tiempo and buen_clima
# qué mensaje imprimirá si hay tiempo y buen clima
# debe mostrar un mensaje si ambas condiciones son verdaderas
#2. Usen un f-string con {} para usar su variable e imprimir un mensaje con la palabra True.
# Usen su imaginación y cambien la frase.
#print(f"Podemos ir a caminar al bosque hoy: {disponibilidad_clima}")
#3. Corre solo esa parte del programa para ver si tiene sentido lo que sale en la terminal. 
# Usando triple comillas puedes probar cada parte del código que corra adecuadamente.
# 4. Aquí el nombre de otra variable. 
# En este caso con el Operador NOT (NO) combinado con OR (O): Invierte el valor de una condición
# ¿Si no hay tiempo y tampoco buen clima?
debe_reprogramar = not tiene_tiempo or not buen_clima
#5 Inventen algo más que imprimir en la pantalla.
# print(f"debo reprogramar la aventura {debe_reprogramar}")

# 6. Una última variable.
# Expresión compleja usando paréntesis para prioridades
# la condición usa los operadores and y or e incluye la cuarta variable
puede_salir = tiene_tiempo and buen_clima and (tiene_dinero or tiene_cupon)
#7. Una ultima frase
#print(f"puedo salir de aventura {puede_salir}")
#8. Ahora sí queremos que solo me aparezca una frase al completar el cuestionario (tienes tiempo, hace buen clima, tienes cupon).
# Este sería un buen momento para utilizar un if statement. Cambia el código para que solo imprima una frase dependendiendo de las respuestas.
# por ejemplo, si al correr el programa con sí sí y no, tal vez solo me diga "sal a caminar por el bosque."
# Para empezar, descomenta las siguientes dos líneas y agrega # en las líneas anteriores que ya no son necesarias. Pero no las borres para la entrega final.


# if tiene_tiempo and buen_clima: 
#     print("sal a caminar")

if puede_salir:
    print("puedes salir de aventura")
else:
    print("puedes planear la aventura para otro día")

print("\ngracias por participar")
# nueve reto final copiando el estilo ya utilizado