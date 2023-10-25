# Utilizar la funcion range() para imprimir una serie de numeros
for value in range(1, 10):
    print(value) # 1...9

for value in range(7):
    print(value) # 0...6

# Utilizando la funcion list() podemos crear una lista de numeros
number_list = list(range(1, 13))
print(number_list)

# Pasando un tercer parametro a la funcion range() podriamos guardar una lista de numeros pares o impares
even_numbers = list(range(2, 10, 2)) # Este tercer valor sumara de 2 en 2 empezando en 2
print(even_numbers)
odd_numbers = list(range(1, 10, 3))
print(odd_numbers) # Este tercer valor sumara de 3 en 3 empezando en 1