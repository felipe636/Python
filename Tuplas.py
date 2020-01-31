"""
Tuplas:
   Una tupla es una coleccion ordenada e inmutable, las tuplas en python se
   escriben entre corchetes.
"""

#Ejemplo de una tupla
Tupla=('Phone','Tv','Biker')
print(Tupla)


#Para acceder a los elementos de una tupla  se hace referencia al elemento entre
#corchetes
Tupla=('Phone','Tv','Biker')
print(Tupla[1])


#Indexacion negativa
Tupla=('Phone','Tv','Biker')
print(Tupla[-1])

#Rangos es basicamente de la misma forma que en las listas
Tupla=('Phone','Tv','Biker')
print(Tupla[0:3])

#Rangos negativos

Tupla=('Phone','Tv','Biker')
print(Tupla[-3:-1])

#Cambiar de tupla a lista y viceversa
Tupla=('Phone','Tv','Biker')
Lista=list(Tupla) #Convierte la tupla en una lista
print(Lista)
MiTupla=tuple(Lista)  #Vuelve a convertir la lista a una tupla
print(MiTupla)


#Recorrer los elementos de una tupla con un ciclo for
Tupla=('Phone','Tv','Biker')
for i in Tupla:
    print(i)

#Comprobar si exite un elemento en la tupla
Tupla=('Phone','Tv','Biker')
if "door" in Tupla:
    print('Yes, this is')
else:
    print('No, this is not ')

#Para saber la longitus de una tupla use el metodo len()
Tupla=('Phone','Tv','Biker')
print(len(Tupla))

#Las tuplas son inmutables es decir que no se pueden agregar mas elementosa una tupla

#Tuplas con un elemento, es necesario colocar una coma despues del elemento
#Si no le coloca la coma, leera el contenido de la variable como una cadena.
Computer=('Keyboard',)
print(Computer)

"""
#Eliminar elementos de una tupla
#con la palabra del puede eliminar la tupla completa
Tupla=('Phone','Tv','Biker')
del Tupla
print(Tupla)#La salida es un error porque la tupla ya no existe
"""
#Unir dos tuplas
#Con el operador + se pueden unir mas de una tupla
Tupla1=('Phone','Tv','Biker')
Tupla2=('Computer',)
Tupla3=Tupla1+Tupla2
print(Tupla3)

#El constructor tuple(), permite crear una tupla
Computer=tuple(('mouse','keyboard','screen','speakers','phone'))
print(Computer)

"""
Métodos de tupla
Python tiene dos métodos integrados que puede usar en tuplas.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found.
"""
