precio = 3.49
numero_de_chocolates = 7
print('Precio es del tipo:', type(precio))
print('Numero de chocolates es del tipo:', type(numero_de_chocolates))

precio_total = precio * numero_de_chocolates
print('El precio total es:', precio_total)

numero_de_chocolates = numero_de_chocolates + 1
print('Ahora el numero de chocolates es:', numero_de_chocolates)
numero_de_chocolates += 1
print('Ahora el numero de chocolates es:', numero_de_chocolates)
numero_de_chocolates -= 1
print('Ahora el numero de chocolates es:', numero_de_chocolates)

# Cuando tenemos numeros muy grandes o muy pequenos se va a utilizar
# la notacion cientifica
# Ejemplo:
numero_grande = 450000000000000000000000000000000.1
print(numero_grande)
numero_pequeno = 0.00000000000000000000000000000034
print(numero_pequeno)