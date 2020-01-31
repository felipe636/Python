"""

 Sets(conjuntos en español):
              Un conjunto es una coleccion que no esta ordenada ni indexada. En
              python, los conjuntos se escriben entre llaves.
"""

#Crear un conjunto
Vestido={'Camisa','Zapatos','Medias'}
print(Vestido)


#No se puede acceder mediante un indice a un conjunto en python, lo que se
#puede hacer es recorrer ell conjunto

Vestido={'Camisa','Zapatos','Medias'}
for i in Vestido:
    print(i)

#Comprobar si un elemento esta en el conjunto
Vestido={'Camisa','Zapatos','Medias'}
print('Pantalon' in Vestido)

#Una vez creado un conjunto no se puede cambiar sus elementos pero si se puede
#agregar mas elementos

#Para agregar un elemento a un conjunto use el metodo add()
Vestido={'Camisa','Zapatos','Medias'}
Vestido.add('Pantalon')
print('Pantalon' in Vestido)
print('La lista de prendas de vestir es ',Vestido)

#Para agregar mas de un elemento a un conjunto se utiliza el metodo update()
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
print('La lista actualizada de prendas de vestir  es ',Vestido)


#Obtener la longitud de un conjunto (set)
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
print(len(Vestido))


#Remover elementos de un conjunto con el metodo remove()
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
Vestido.remove("Medias") #Si el elemento  a eliminar no existe en el metodo remove() se generara un error
print(Vestido)

#Remover elementos de un conjunto con el metodo discard()
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
Vestido.discard('Camisa')
print(Vestido)

#Tambien se utiliza el metodo pop(), como los conjuntos son desordenados
#el metodo pop() eliminara el ultimo elemento del conjunto.
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
Remove=Vestido.pop()
print(Vestido)

#El metodo clear() vacia todos los elementos del conjunto
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
Vestido.clear()
print(Vestido)

"""
#La palabra del eliminara todo el conjunto por completo
Vestido={'Camisa','Zapatos','Medias'}
Vestido.update(['Chaqueta','Short'])
del Vestido
print(Vestido)#La salida es un error porque el conjunto no existe
"""

#Para unir dos conjuntos una de las formas es utilizando el metodo  union()
Vestido={'Camisa','Zapatos','Medias'}
Musica={'Bolero','Vallenato','pop','electronica'}
Union=Vestido.union(Musica) #Se crea otra variable para almacenar la union de los conjuntos
print(Union)


#Para unir dos conjuntos tambien se utiliza el metodo update()
Vestido={'Camisa','Zapatos','Medias'}
Musica={'Bolero','Vallenato','Vallenato','pop','electronica'}#tanto el metodo union() como el metodo update() eliminaran los elementos duplicados.
Vestido.update(Musica)
print(Vestido)

#Tambien se puede utilizar el constructor set() para hacer un conjunto
Vestido=set(('Camisa','Zapatos','Medias'))
print(Vestido)

"""
Establecer métodos
Python tiene un conjunto de métodos integrados que puede usar en conjuntos.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""
