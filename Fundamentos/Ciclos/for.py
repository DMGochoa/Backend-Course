# Los ciclos 'for' en Python son como una persona regando plantas en un jardín
# Recorren cada elemento en una secuencia de manera ordenada

# Ejemplo de un ciclo 'for'

frutas = ["manzana", "banana", "cereza"]
print("Inicio del ciclo for")

# Este ciclo recorrerá cada elemento de la lista frutas
for fruta in frutas:
    print(f"Ahora la fruta es: {fruta}")

print("Fin del ciclo for")

# Los ciclos 'for' son ideales cuando conocemos el número de veces que queremos ejecutar un bloque de instrucciones

# Uso de 'for' con la función range() para generar una secuencia de números
print("\nContando hasta 5:")

for numero in range(5):  # Genera números de 0 a 4
    print(numero)

# También podemos usar 'for' para iterar sobre strings
palabra = "Python"
print("\nLetras en la palabra Python:")

for letra in palabra:
    print(letra)
