# Conceptos aprendidos: Concatenación de strings

nombre = 'Diego'
apellido = 'Moreno'

# Concatenación de strings
nombre_completo = nombre + apellido
print(nombre_completo)
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

# Apostrofe en un string
mensaje = "I'm Diego"
# Error: mensaje = 'I'm Diego'
print(mensaje)

# formatos de strings
plantilla = 'Hola, mi nombre es ' + nombre + ' y mi apellido es ' + apellido
print('v1', plantilla)
plantilla = 'Hola, mi nombre es {} y mi apellido es {}'.format(nombre, apellido)
print('v2', plantilla)
plantilla = f'Hola, mi nombre es {nombre} y mi apellido es {apellido}'
print('v3', plantilla)

# Ahora hagan lo mismo de dar un formato pero pidiendo los datos al usuario
# utilicen la funcion input() y pidan nombre, apellido y edad.

# Si un elementro esta en un string
texto = 'Python es un lenguaje de programacion muy poderoso y sencillo de aprender'
print('Python' in texto)
print('python' in texto)
print('Python' not in texto)

# tamano de un string
texto = "hola geNte!"
tamano = len(texto)
print(tamano)
print(texto, texto.lower())
print(texto, texto.upper())
print(texto, texto.capitalize())
print(texto, texto.title())
print('a:', texto.count('a'))
print(texto.swapcase())
print(texto.startswith('ho'))
print(texto.endswith('sencillo'))
print(texto.find('gente'))
print(texto.replace('Python', 'JavaScript'))

# Slicing o rebanado
texto = 'Python es un lenguaje de programacion muy poderoso y sencillo de aprender'
print(texto[0])
print(texto[1])
print(texto[len(texto) - 1])
print(texto[-1])
print(texto[0:6])
print(texto[:6])
print(texto[7:])
print(texto[2:15:2])

texto = '234'
print(texto.isnumeric())


