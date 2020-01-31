Computer = ["mouse","cpu","keyboard"]
Device=Computer.copy()
print(Device)


Computer = ["mouse","cpu","keyboard"]
Computer.clear()
print(Computer)

#Tambien se puede hacer una copia de una lista con el metodo list()
Computer = ["mouse","cpu","keyboard"]
MyComputer=list(Computer)
print(MyComputer)


#Unir dos listas en python
Numeros=[1,2,3,4,5,6]
Numeros2=[7,8,9,10]
Numeros3=Numeros+Numeros2
print(Numeros3)

#Otra forma de agregar los elementos de una lista a otra
Computer = ["mouse","cpu","keyboard"]
Numeros=[1,2,3,4,5,6]
for var in Numeros:
    Computer.append(var)

print(Computer)

#Otra forma de agragar elementos de una lista a otra es con el metodo extend()
Computer = ["mouse","cpu","keyboard"]
Numbers=[1,2,3,4,5,6]

Computer.extend(Numbers)
print(Computer)

#Tambien se puede utilizar el constructor list()
Numbers=[1,2,3,4,5,6]
Numbers=list((45,12,78,25))
print(Numbers)

"""
Métodos de lista
Python tiene un conjunto de métodos integrados que puede usar en las listas.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""


