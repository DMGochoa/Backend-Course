# Los sets en Python son usados para almacenar colecciones de elementos únicos y desordenados
# Se definen utilizando llaves {} o la función set()

# Creando un set de frutas
mi_set = {"manzana", "banana", "cereza"}
print(f"Set original: \n{mi_set}")

# Los sets no tienen un orden fijo, ni índices
# Intentar acceder a un elemento por índice producirá un error

# Agregando elementos al set
mi_set.add("naranja")
print(f"\nSet despues de agregar 'naranja': \n{mi_set}")

# Agregando múltiples elementos (otros sets) con update()
otras_frutas = {"pina", "mango", "papaya"}
mi_set.update(otras_frutas)
print(f"\nSet después de agregar otras frutas: \n{mi_set}")

# Eliminando elementos con remove() o discard(), la diferencia es que remove arrojará un error si el elemento no existe
mi_set.remove("banana")
print(f"\nSet despues de remover 'banana': \n{mi_set}")
mi_set.discard("kiwi")  # No arroja error si "kiwi" no está en el set
print(f"\nSet despues de descartar 'kiwi': \n{mi_set}")

# Iterando sobre un set
print("\nIterando sobre el set:")
for fruta in mi_set:
    print(fruta)

# Comprobando si un elemento está en el set
if "mango" in mi_set:
    print("\n'Mango' esta en el set")

# Uniendo sets con union() o update()
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}
set_unido = set_1.union(set_2)
print(f"\nUnion de set_1 y set_2: \n{set_unido}")

# La diferencia entre sets con difference()
print(f"\nDiferencia entre set_unido y mi_set: \n{set_unido.difference(mi_set)}")

# Intersección de sets con intersection()
print(f"\nInterseccion entre set_unido y otras_frutas: \n{set_unido.intersection(otras_frutas)}")

# Los sets también pueden tener elementos de diferentes tipos
set_variado = {"manzana", 34, True, "123"}
print(f"\nSet con elementos variados: \n{set_variado}")

# Tamaño de un set con len()
print(f"\nTamano del set mi_set: \n{len(mi_set)}")
