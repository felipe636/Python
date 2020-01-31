#Arrays in Python
"""
Python no tiene soporte integrado para matrices, pero las listas de python se 
pueden usar en su lugar.
"""

#matrices
"""
Las matrices se utilizan para almacenar multiples valores en una sola varible
"""

#Crear una matriz que contenga nombres de automoviles
Carros=["BMW","Ferrari","Ford"]
print(Carros[0])

"""
Una matriz es una variable especial, que puede contener mas de una valor a la vez.
Para acceder a los valores de una matriz se hace la referencia con el 
numero de indice.
"""

#Modificando el valor de la posicion  de la matriz
Carros[0]='Hunday'
print(Carros)

#La longitud de una matriz

"""
Para devolver la longitud de una  matriz( el numero de elementos de una}
matriz) se utiliza el metodo len()
"""
Cars=len(Carros)
print(Cars)

#Recorrer una matriz con un bucle For
"""
Puede usar el bucle for in para recorrer todos los elementos de una 
matriz.
"""
for i in Carros:
    print(i)
    
#Agregar elementos a una matriz
"""
Puede usar el metodo append() para agregar elementos a una matriz.
"""

Carros.append("BMW")
print(Carros)

#Eliminar elementos de una matriz 
"""
Puede usar el metodo pop() para eliminar elementos de una matriz
"""

Carros.pop(2)
print(Carros)

#Tambien puede eliminar elementos de una matriz con el metodo remove()

Carros.remove('Hunday')
print(Carros)

"""
Métodos de matriz
Python tiene un conjunto de métodos integrados que puede usar en listas / matrices.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
