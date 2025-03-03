# match (significa coincidencia. Funciona como el condicional if pero ....

codigo = input("Introduzca un código HTTP: ")

match codigo:
    case "200":
        print('Todo ok.')
    case "301":
        print('Movimiento permanente de la página.')
    case "302":
        print('Movimiento temporal de la página.')
    case "404":
        print('Página no encontrada')
    case "500":
        print('Error interno del servidor.')
    case "503":
        print('Servicio no disponible.')
    case _:
        print('Código no disponible')

