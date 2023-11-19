# En este caso solo se tiene dos valores posibles, verdadero o falso.
tiene_arepas = True
print('El tipo de dato de la variable tiene_arepas es:', type(tiene_arepas))
tiene_queso = False
print('Tiene arepas?', tiene_arepas)
print('Tiene queso?', tiene_queso)
print('Puedo hacer arepas con queso?', tiene_arepas and tiene_queso)
print('Puedo hace una arepa sin queso?', tiene_arepas or tiene_queso)

# Negacion de una expresion
print('No tiene arepas?', not tiene_arepas)