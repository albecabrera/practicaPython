colores = ["rojo", "azul", "verde", "amarillo"]

print("---LISTADO DE COLORES---")

for color in colores:
    # Condición para romper la ejecución
    if color == "azul":
        break # Finaliza el bucle antes de tiempo

    # Si no entra en el if, se imprime el valor iterado
    print(f"-Color {color}.")