# el continue 
colores = ["rojo", "azul", "verde", "amarillo"]
print("---LISTADO DE COLORES---")

for color in colores:
    if color == "azul" or color == "verde":
        continue # omite una iteración

    # Si no entra en el if, se imprime el valor iterado
    print(f"-Color {color}.")

    colores = ["rojo", "azul", "verde", "amarillo"]
print("---LISTADO DE COLORES---")

