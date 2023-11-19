# El módulo collections proporciona alternativas especializadas a los contenedores de Python incorporados

from collections import Counter

# Usando Counter para contar la ocurrencia de cada elemento en una lista
lista = ["manzana", "banana", "cereza", "manzana", "cereza", "cereza"]
conteo = Counter(lista)
print(conteo)  # Muestra la frecuencia de cada fruta en la lista

# functools es útil para funciones de orden superior, que actúan o devuelven otras funciones

from functools import reduce

# Usando reduce para calcular el producto de una lista de números
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x*y, numeros)
print(producto)  # Muestra 120 (1*2*3*4*5)

# random proporciona funciones para generar números aleatorios
import random
# Generando un número aleatorio entre 0 y 100
numero_aleatorio = random.randint(0, 100)
print(numero_aleatorio)

# math ofrece una amplia gama de funciones matemáticas
import math
# Calculando la raíz cuadrada de un número
raiz = math.sqrt(16)
print(raiz)  # Muestra 4.0

# time se utiliza para manipular representaciones de tiempo
import time
# Imprimiendo la hora actual
hora_actual = time.ctime()
print(hora_actual)

# sys proporciona acceso a algunas variables y funciones interactuando con el intérprete Python
import sys
# Imprimiendo la versión de Python en uso
print(sys.version)

# os permite interactuar con el sistema operativo
import os
# Listando archivos en el directorio actual
archivos = os.listdir('.')
print(archivos)

# re se utiliza para trabajar con expresiones regulares
import re
# Buscando una palabra en una cadena
resultado = re.search("hola", "hola mundo")
print(resultado.group())  # Imprime 'hola' si encuentra la palabra




