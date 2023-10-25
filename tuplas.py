# Tuplas -> Son inmutables, su valor NO puede cambiar, a diferencia de las listas las tuplas se definen con parentesis ()

car_brands = ('seat', 'audi', 'bmw')

for car in car_brands:
    print(car.title())

# Como los valores son inmutables, para modificar un valor hay que reasignar los valores a la tupla

car_brands = ('seat', 'audi', 'honda')

for car in car_brands:
    print(car.title())