# Los ciclos 'while' en Python son como un hámster corriendo en una rueda
# Continúan ejecutando un conjunto de instrucciones mientras una condición sea verdadera

# Ejemplo de un ciclo 'while'

contador = 0
print("Inicio del ciclo while")

# Este ciclo se ejecutará mientras contador sea menor a 5
while contador < 5:
    print(f"El valor del contador es: {contador}")
    contador += 1  # Incrementamos el contador

print("Fin del ciclo while")

# Los ciclos 'while' son útiles cuando no sabemos cuántas veces necesitamos ejecutar el bloque de instrucciones

# Uso de 'while' con una condición de parada
# Este ciclo se detendrá cuando el usuario escriba 'salir'

entrada = ""
while entrada.lower() != "salir":
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    print(f"Escribiste: {entrada}")

print("Has salido del ciclo")
