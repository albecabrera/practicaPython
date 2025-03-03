# Para que se utilizan las tuplas 
# Para datos constantes que no son modificables

tupla = ("rojo", "azul", "verde")

print(tupla[1]) #azul
# Las tuplas son inmutables
print(tupla.index("rojo"))

numero1 = 10
numero2 = 20.5
print(type(numero1 + numero2))
print(type(numero1))
print(type(numero2))
print() # asi se deja un espacio entre líneas. 
print(type(numero1 + int(numero2)))



numero_1 = input("Introduzca el primer número: ") # Esto es un string
numero_2 = input("Introduzca el segundo número: ") # Esto también es un string

suma = numero_1 + numero_2
print(f'El resultado de la suma es: {suma}.') # el resultado final es también un string

numero_1 = int("10")
numero_2 = int("30")
suma = numero_1 + numero_2
print(f"El resultado de la suma es: {suma} ")

numero_1 = float(input("Introduzca el primer número: ")) # Esto es un string
numero_2 = float(input("Introduzca el segundo número: ")) # Esto también es un string

suma = numero_1 + numero_2
print(f'El resultado de la suma es: {suma}.')



