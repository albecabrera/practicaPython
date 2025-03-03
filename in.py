# se utiliza en bucles y condicionales para ver si hay coincidencias

cadena = "Hola, mundo!"

lista_caracteres = list(cadena)

print(lista_caracteres)

saludo = "Hola"

print(saludo[0])
print(saludo[1])
print(saludo[2])
print(saludo[3])

# Elemento de secuencia
texto = "La programación es el arte de crear algo de la nada"

# Variable para buscar coincidencia
buscar = "arte" in texto
print(buscar)


# Elemento con secuencia
colores = ["rojo", "verde", "azul", "amarillo"]

print("---LISTADO DE COLORES---")

for color in colores:
    print(f"-{color}")
    