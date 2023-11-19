edad = '26'
print('El tipo de dato de la variable edad es:', type(edad))
edad = int(edad)
print('El tipo de dato de la variable edad es:', type(edad))
edad = True
print('El tipo de dato de la variable edad es:', type(edad))
# Error: int('Diego')
print('Hola ' + str(edad))
print(20 + 23)
# Error: print('Hola ' + 20)

# Transformacion de tipos de datos booleanos
# False
print(bool(0))
print(bool(''))
print(bool(None))
print(bool(False))
# True
print(bool(1))
print(bool('Hola'))
print(bool(-1))
print(bool(2))
print(bool(True))
