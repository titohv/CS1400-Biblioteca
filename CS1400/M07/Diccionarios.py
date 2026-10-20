num_salon = {
    "Murphy": 304,
    "Feiz": 336,
    "Mack": 207,
    "Ball": 227,
    "Bristow": 321,
    "Cruz": 101
}

print("La longitud es", len(num_salon))

# Agregar un elemento adicional al diccionario
num_salon["Valle"] = 216
print("La longitud ahora es ", len(num_salon))

print( num_salon.get("Valle") )
print( num_salon["Murphy"])