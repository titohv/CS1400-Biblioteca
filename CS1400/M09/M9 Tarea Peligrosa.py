"""lst = [1, 3, 7, 3]

# Entrada de datos
num = int(input("Ingrese un número entero: "))

# Operación 1: División
#print(10 / num)

# Operación 2: Acceso a Lista
print(lst[num]) 

# Operación 3: Continuación
print("El programa continuó con éxito.")



try:
    lst = [1, 3, 7, 3]
    num = int(input("Ingrese un número entero: "))
    
    print(10 / num)
    print(lst[num])

#except ValueError:
#    print("❌ Error: Debes ingresar un número entero válido (sin letras).")
#except:
#    print("❌ Ocurrió un error general.")


except ZeroDivisionError:
    print("❌ Error: No es posible dividir entre cero.")
except IndexError:
    print("❌ Error: Índice fuera de rango en la lista.")

print("El programa continúa su ejecución normal...")


4.	Ejecuta el código anterior e ingresa "dos". ¿Qué mensaje se imprime? ¿Se ejecuta la última línea de "El programa continúa..."?
si se ejecuta la última línea.
5.	Ejecuta el código e ingresa 0. ¿Por qué se activa el mensaje "Ocurrió un error general" en lugar del de ValueError?
por error en la división entre cero
6.	Modificación de código 1: Agrega un bloque except ZeroDivisionError específico con el mensaje: "❌ Error: No es posible dividir entre cero."

except ZeroDivisionError:
    print("❌ Error: No es posible dividir entre cero.")
except IndexError:
    print("❌ Error: Índice fuera de rango en la lista.")

print("El programa continúa su ejecución normal...")

7.	Modificación de código 2: Identifica el tipo de error que ocurre al intentar acceder a un índice inexistente en la lista lst (al ingresar 100). Agrega un bloque except específico para capturar dicho error con un mensaje descriptivo.
el error que ocurre al intentar acceder a un índice inexistente en la lista es IndexError
8.	Pega tu código corregido con las 3 excepciones específicas aquí.

try:
    lst = [1, 3, 7, 3]
    num = int(input("Ingrese un número entero: "))
    
    print(10 / num)
    print(lst[num])

except ZeroDivisionError:
    print("❌ Error: No es posible dividir entre cero.")
except IndexError:
    print("❌ Error: Índice fuera de rango en la lista.")

print("El programa continúa su ejecución normal...")


import traceback

try:
    num = int(input("Ingrese un número: "))
    print(10 / num)
except ValueError as e:
    print("⚠️ Capturamos un ValueError. Detalle técnico:")
    s = traceback.format_tb(e.__traceback__)
    print(s)

print("El programa continúa...")






print("--- Validación de Rango ---")
num = 0

while num < 1 or num > 10:
    try:
        num = int(input("Ingrese un número del 1 al 10: "))
        
        if num < 1 or num > 10:
            raise Exception("El número está fuera del rango permitido.")
            
    except ValueError:
        print("❌ Error: Formato incorrecto, se esperaba un número.")
    except Exception as e:
        print(f"⚠️ Error de validación: {e}")
    finally:
        print("🔔 [Bloque Finally] Intento de entrada finalizado.")

print(f"¡Número válido ingresado con éxito! ({num})")

"""




def calculadora_segura():
    print("\n--- Calculadora Robusta ---")
    
    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operador permitido
            if op not in ['+', '-', '*', '/']:
                # TODO 1: Lanza (raise) un ValueError con el mensaje "Operador no válido"
                raise ValueError("Operador no válido")
                pass

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"✅ Resultado: {resultado}")
            break  # Salir del bucle si el cálculo se realizó con éxito

        # --- MANEJO DE EXCEPCIONES ---

        # TODO 2: Captura el error de formato cuando el usuario ingresa texto en lugar de números
        # except ...:
        #     print("❌ Error: Ingrese valores numéricos válidos.")

        # TODO 3: Captura la división por cero
        # except ...:
        #     print("❌ Error: No se puede dividir entre cero.")

        # TODO 4: Captura el ValueError (generado por el operador inválido) y muestra e
        # except ValueError as e:
        #     print(f"❌ Error de entrada: {e}")

        except Exception as e:
            print(f"❌ Error no esperado: {e}")
        
        finally:
            # TODO 5: Muestra siempre un mensaje de cierre de intento
            pass

calculadora_segura()


