"""
try:
    suma = 0
    # 1. Abre el archivo numeros.txt aquí
    #archivo = open('numeros.txt', 'r')
    from pathlib import Path
    archivo = open(Path(__file__).parent / 'numeros.txt', 'r')

    for line in archivo:
        # 2. Convierte la línea a entero
        num = int(line.strip())
        print(num)
        suma += num

    print(f"Total: {suma}")
    archivo.close()

except Exception as err:
    print(err)


7. ¿Cuál es el resultado de la suma de los números proporcionados?
invalid literal for int() with base 10: '0, 1, 12, 35, 8, 13, 21, 34, 55'
8. Si agregas la palabra "Python" al archivo de texto, ¿qué error muestra el programa?
invalid literal for int() with base 10: 'Python 0, 1, 12, 35, 8, 13, 21, 34, 55'
9. ¿Por qué es necesario usar .strip() antes de convertirla a número?
porque .strip() elimina los espacios en blanco y saltos de linea que podrian causar errores al convertir la cadena a un numero
10. Si el archivo tiene 9 números, ¿cuántas veces se ejecuta el bloque dentro del for?
9 veces una por cada numero en el archivo




import json

usuario = {
    "nombre": "Estudiante",
    "habilidades": ["Python", "HTML"],
    "activo": True
}

# GUARDAR
with open('datos.json', 'w') as f:
    json.dump(usuario, f, indent=4)

# LEER
with open('datos.json', 'r') as f:
    datos = json.load(f)
    print(f"Usuario: {datos['nombre']}")


11. ¿Qué hace la función json.dump()?
hace que el diccionario de Python se guarde en un archivo en formato JSON
12. ¿Cuál es la ventaja de usar with open(...) en lugar de .close()?


"""