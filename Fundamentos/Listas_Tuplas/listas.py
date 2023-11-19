numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(type(numbers))

# Podemos guardar diferentes elementos
lista_qehaceres = ['Sacar al perro', 'Lavar los trastes', 'Hacer la tarea']
print(lista_qehaceres)

# Podemos guardar diferentes tipos de datos
lista_mixta = ['Hola', 1, 2.5, True]

# Extraer elementos de una lista
print(lista_qehaceres[0])
# Podemos mutar las listas
lista_qehaceres[0] = 'Sacar al gato'
print(lista_qehaceres)
#Slicing
print(lista_qehaceres[0:2])
# Operador in
print('Sacar al gato' in lista_qehaceres)

# Algunos metodos de las listas
# CRUD, crear, Leer, actualizar y borrar
# Crear
mi_lista = [1, 2, 3, 4, 5]
# Leer
print(mi_lista[0])
# Actualizar
mi_lista[0] = 0
mi_lista[-1] = 6
print(mi_lista)
# Agregar elementos
mi_lista.append(7)
print(mi_lista)
# agrega el elemento y el resto se corre a la derecha
mi_lista.insert(0, 'Hola soy un string')
print(mi_lista)

# Concatenar listas
mi_lista = mi_lista + [8, 9, 10]
print(mi_lista)
# Encontrar el indice de un elemento
print(mi_lista.index('Hola soy un string'))

# Eliminar elementos
# Elimina el ultimo elemento
mi_lista.pop()
print(mi_lista)
# Elimina el elemento en el indice que le pasemos
mi_lista.pop(1)
print(mi_lista)

# Elimina el elemento que le pasemos
mi_lista.remove('Hola soy un string')
print(mi_lista)

