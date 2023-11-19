# Las funciones en Python son como pequeñas "fábricas" que toman algunos materiales (parámetros),
# trabajan con ellos y devuelven un producto (resultado)

# Definición de una función simple

# Esta función imprime un mensaje de bienvenida
def saludar():
    print("¡Hola! Bienvenido al curso de Python.")

# Llamando a la función
saludar()  # Esto ejecutará el código dentro de saludar()

# Función con parámetros

# Esta función toma un nombre y lo imprime
def saludar_nombre(nombre):
    print(f"¡Hola, {nombre}!")

# Llamando a la función con un parámetro
saludar_nombre("Juan")  # Imprime: ¡Hola, Juan!

# Función que devuelve un valor

# Esta función calcula la suma de dos números y devuelve el resultado
def sumar(a, b):
    return a + b

# Llamando a la función y almacenando su resultado
resultado = sumar(5, 3)  # resultado es ahora 8
print(f"El resultado de la suma es: {resultado}")

# Funciones con parámetros por defecto

# Esta función saluda con un mensaje, que puede ser personalizado
def saludo_personalizado(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}, {mensaje}")

# Llamando a la función con y sin el parámetro por defecto
saludo_personalizado("Ana")  # Imprime: Hola Ana, ¡Bienvenido!
saludo_personalizado("Carlos", "¡Qué bueno verte de nuevo!")  # Imprime: Hola Carlos, ¡Qué bueno verte de nuevo!

# Funciones que aceptan un número variable de argumentos

# Esta función suma cualquier cantidad de números
def suma_varios(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

# Llamando a la función con diferentes cantidades de argumentos
print(f"Suma de 1, 2, 3: {suma_varios(1, 2, 3)}")  # Suma de 1, 2, 3: 6
print(f"Suma de 4, 5, 6, 7: {suma_varios(4, 5, 6, 7)}")  # Suma de 4, 5, 6, 7: 22
