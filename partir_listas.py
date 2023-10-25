# Partir listas

numbers = list(range(1, 31))

# Trozo de la lista del 1 al 5
numbers_slide_1 = numbers[0:5]
print(numbers_slide_1)

# Trozo de la lista del 11 al 15
numbers_slide_2 = numbers[10:15]
print(numbers_slide_2)

# Trozo de la lista del 1 al 10
numbers_slide_3 = numbers[:10]
print(numbers_slide_3)

# Trozo de la lista del 20 al 30
numbers_slide_4 = numbers[19:]
print(numbers_slide_4)

# Trozo de la lista del 27 al 30
numbers_slide_5 = numbers[-4:]
print(numbers_slide_5)

# Recorrer un trozo utilizando un bucle for
names = ['Antonio', 'Ruiz', 'Benito', 'Chula', 'Arya', 'Patricia']
for name in names[:2]:
    print(name)

# Copiar una lista
names_copy = names[:]
print(names_copy)