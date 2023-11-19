# Condicionales

if True:
    print("Se cumple la condición")

if False:
    print("No se cumple la condición")
else:
    print("Se ejecuta otra cosa")


numero = int(input("Escribe un número: "))

if numero < 0:
    print("El número es negativo")
elif numero < 10:
    print("El número es positivo y menor a 10")
else:
    print("El número es positivo y mayor a 10")

texto = 'Python es un lenguaje de programacion muy poderoso y sencillo de aprender'
if 'Python' in texto:
    print('Python esta en el texto')

# Creen un programa que le pida al usuario un número e imprima si es par o impar.
# Haz un juego de piedra papel o tijera contra la computadora.