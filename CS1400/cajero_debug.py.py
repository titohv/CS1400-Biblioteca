# --- PROGRAMA DE CAJERO AUTOMÁTICO ---
saldo_actual = 1000

# -------------------------------------------------------------------
# ERROR 1: RUNTIME ERROR (TypeError)
# input() devuelve una cadena de texto (str). Al intentar operar
# matemáticamente con un entero o flotante, el programa falla en ejecución.
# INSTRUCCIÓN: Con tu pareja, investiga cómo corregir el casting de datos.
# Agrega un comentario indicando la solución y dónde/cómo encontraron la información.
# -------------------------------------------------------------------
# me parece que debemos tener datos de tipo float para la entrada para realizar operaciones matematicas
retiro = float(input("¿Cuánto dinero deseas retirar?: "))


# -------------------------------------------------------------------
# ERROR 2: LOGIC ERROR
# Nota: Si corrigen el tipo de dato arriba, este bloque correrá sin lanzar un error explícito.
# Sin embargo, ¿el comportamiento del cajero es correcto? No se debe permitir retirar dinero
# si no se tiene saldo suficiente.
# INSTRUCCIÓN: Corrijan la lógica del condicional y expliquen en un comentario por qué hicieron el cambio.
# -------------------------------------------------------------------
if retiro <= saldo_actual:
    # unicamente se permite retirar si el saldo es suficiente para cubrir el retiro
    print("Extracción exitosa.")
    saldo_actual = saldo_actual - retiro
    print(f"Tu nuevo saldo es: {saldo_actual}")
else:
    print("Saldo insuficiente.")


# -------------------------------------------------------------------
# ERRORES 3 y 4: SYNTAX ERROR / LOGIC ERROR
# INSTRUCCIÓN: Usen el depurador de VS Code para detectar los errores restantes en la línea final.
# -------------------------------------------------------------------
#faltaba el parentesis de cierre
print("Gracias por usar el cajero")