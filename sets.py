'''
Listas desordenadas
Datos inmutables
Se pueden eliminar y añadir datos
'''
saludo = "hola"

print(saludo[0])
print(saludo[1])
print(saludo[2])
print(saludo[3])



# Crear un set
mi_set = {"manzana", "banana", "cereza"}

# Añadir un elemento
mi_set.add("naranja")

# Eliminar un elemento
mi_set.remove("banana")

# Comprobar si un elemento está en el set
print("manzana" in mi_set)  # True

# Imprimir el set
print(mi_set)

set_colores ={"rojo", "verde", "azul", "amarillo", "rojo", "rojo"}

set_colores.add("violeta") # agrega un elemento
set_colores.remove("rojo") # elimina un elemento

print(set_colores)

# se pueden almacenar listas dentro de otras listas
lista_numeros = [10,20,30,40]

lista2 = [10, lista_numeros]

print(lista2)

# not  
print(True)
print(not True)
print(not False)

