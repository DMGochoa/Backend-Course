# Los diccionarios son usados para almacenar datos de la manera llave:valor (key:value)
# Podemos definir un diccionario con llaves {} y dentro de ellas pares de datos que queramos almacenar

mi_auto = {"brand": "Ford", "model": "Mustang", "year": 1969}

# Un diccionario es una colección ordenada, modificable y que no permite duplicados (en los valores de llave)

# Podemos verificar que el orden de ingreso de datos se conserva:
print(f"Diccionario mi_auto: \n{mi_auto}")

# Podemos agregar valores
mi_auto["color"] = "red"
print(f"\nDiccionario mi_auto con color: \n{mi_auto}")

# Podemos cambiar valores
mi_auto["color"] = ["red", "white"]
print(f"\nDiccionario mi_auto con color como lista: \n{mi_auto}")

# Podemos eliminar valores
mi_auto.pop("color")
print(f"\nDiccionario mi_auto sin color: \n{mi_auto}")

# Inclusive podemos tener diccionarios que contengan otros diccionarios!
mi_familia = {
    "padre" : {"nombre" : "Luis",
               "edad" : 40},
    "madre" : {"nombre" : "Maria",
               "edad" : 35},
    "hermano" : {"nombre" : "Diego",
                 "edad" : 27}
}
print(f"Esta es mi familia:\n{mi_familia}")

# Podemos iterar sobre el diccionario (llaves por defecto)
print("\nDiccionario mi_auto:")
for x in mi_auto:
    print(x)
    
# Podemos iterar sobre las llaves explicitamente
print("\nLlaves:")
for x in mi_auto.keys():
    print(x)

# Podemos iterar sobre los valores
print("\nValores:")
for x in mi_auto.values():
    print(x)
    
# Podemos iterar sobre llaves y valores
print("\nPares (llave:valor):")
print("Llave : Valor")
for x, y in mi_auto.items():
    print(f"{x} : {y}")
    
