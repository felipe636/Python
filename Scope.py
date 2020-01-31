#Scope o alcance en python
"""
Una variable solo está disponible desde el interior de la region en la que se
crea. esto se llama scope(alcance).
"""

#Alcance local
"""
Una variable creada dentro de una funcion pertenece al ambito local de esa
funcion, y solo puede usarse dentro de esa funcion.
"""

def myfuction():
    Var=45
    print(Var)

myfuction()


#Funcion dentro de una funcion
"""
Como se muestra en el ejemplo anterior la variable es local y no puede trabajarse
por fuera de esa funcion, pero si en una funcion interna.
"""
def myfuction():
    Var=45
    def myinnerfuction():
        print(Var)
    myinnerfuction()
myfuction()

#Alcance global
"""
Una variable creada en el cuerpo principal del codigo en python es una variable
global y pertenece al ambito global.

Las variables globales están disponibles desde cualquier ambito, global y local
"""

Var=76

def myfuction():
    Var2=86
    Suma=Var+Var2
    print(Suma)

myfuction()
print(Var)

#Nombrar las variables
"""
Si opera con el mismo nombre de variable dentro y fuera de una función,
Python las tratará como dos variables separadas, una disponible en el
ámbito global (fuera de la función) y otra disponible en el ámbito
local (dentro de la función).
"""
Var=76

def myfuction():
    Var=45
    print(Var)

myfuction()
print(Var)


#Palabra clave 'global'
"""
Si necesita crear una variable global, pero esta atascado en el ambito local,
puede usar la palabra clave 'global'.

La palabra clave 'global' hace que la variable sea global.
"""

def myfuction():
    global var
    var=99

myfuction()
print(var)


#Tambien puede cambiar el valor de la variable global dentro de una funcion

var=234

def myfuction():
    global var
    var=78

myfuction()
print(var)








