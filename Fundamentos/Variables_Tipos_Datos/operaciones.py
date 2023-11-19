# Operadores aritmeticos
"""
PEMDAS
Parentesis
Exponentes
Multiplicacion
Division
Adicion
Sustraccion
"""
print('Operadores aritmeticos')
# suma: +
print('5 + 3 =', 5 + 3)
# resta: -
print('5 - 3 =', 5 - 3)
# multiplicacion: *
print('5 * 3 =', 5 * 3)
# division: /
print('5 / 3 =', 5 / 3)
# division entera: //
print('5 // 3 =', 5 // 3)
# modulo: %
print('5 % 3 =', 5 % 3)
# potencia: **
print('5 ** 3 =', 5 ** 3)

print('Operadores relacionales')
# Operadores relacionales
# igual que: ==
print('5 == 3:', 5 == 3)
# diferente que: !=
print('5 != 3:', 5 != 3)
# mayor que: >
print('5 > 3:', 5 > 3)
# menor que: <
print('5 < 3:', 5 < 3)
# mayor o igual que: >=
print('5 >= 3:', 5 >= 3)
# menor o igual que: <=
print('5 <= 3:', 5 <= 3)

print('Operadores logicos')
# Operadores logicos
# y: and
print('True and False:', True and False)
# o: or
print('True or False:', True or False)
# negacion: not
print('not True:', not True)

print('Comparacion de floats')
# Comparacion de floats
valor1 = 0.1 + 0.1 + 0.1
valor2 = 0.3
print('0.1 + 0.1 + 0.1 == 0.3:', valor1 == valor2)
print(valor1, valor2)
# Solucion por tolerancia
print('Solucion por tolerancia')
tolerancia = 0.000000001
print('0.1 + 0.1 + 0.1 == 0.3:', abs(valor1 - valor2) < tolerancia)
