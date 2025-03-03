'''
Los operadores lógicos
'''
# and, or, not para obtener un resultado...
# ==, =|

a = 10
b = 15

comparacion = a != b
print(comparacion)

# >, < => mayor que o menor que

comparacion = a > b
print(comparacion) # 10 no es mayor que 15, por lo tanto es falso

# >=, <= mayor o menor igual que
comparacion = a >= b
print(comparacion)

# and
a = 15
b = 17
c = 13

# comparaciones
comparacion_1 = a < b and b > c # True
comparacion_2 = a > b and b > c # False

# comprobamos los resultados 
print(comparacion_1)
print(comparacion_2)


# verdadero o falso

