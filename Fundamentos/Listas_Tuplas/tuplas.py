numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers)
print(type(numbers))
strings = ('Hola', 'Mundo', 'Desde', 'Python', 'Hola')
print(strings)
print(type(strings))

# Las tuplas son inmutables esto quiere decir que no podemos modificarlas
# numbers[0] = 0 esto nos va a dar un error
# Podemos extraer elementos de una tupla
print(numbers[0])
print(numbers.index(1))
print(strings.count('Hola'))


my_list = list(numbers)
print(my_list)
my_list.append(10)
numbers = tuple(my_list)
print(numbers)
# Ahora modifiquen el juego de piedra papel o tijera donde el usuario pueda
# elegir de una tupla de opciones