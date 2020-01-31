#Objetos y clases 
"""
Python es un lenguaje de programación orientado a objetos.
Casi todo en Python es un objeto, con sus propiedades y métodos.
Una clase es como un constructor de objetos, o un "plano" para crear
objetos.
"""

#Crear una clase en python 
"""
Para crear una clase en python se utiliza la palabra clave 'class'
"""

class Suma:
    x=5

print(Suma)

#Crear un objeto
"""
Ahora podemos usar la clase llamada Suma para crear objetos, en este 
caso se imprimira en un objeto llamado Numero el valor de x.
"""

Numero=Suma()
print(Numero.x)

#La funcion __init__()
"""
Los ejemplos anteriores son clases y objetos en su forma más simple, 
y no son realmente útiles en aplicaciones de la vida real.

Todas las clases tienen una funcion llamada __init__(), que siempre
se ejecuta cuando se inicia la clase.

Use la funcion __init__() para asignar valores a las propiedades del
objeto u otras operaciones que sean necesarias cuando se crea el objeto
"""

#Cree una clase llamada Persona, use la funcion __init__() para asignar
#valores para nombre y edad.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        

Individuo=Persona('Juan', 59)

print(Individuo.nombre)
print(Individuo.edad)

#La funcion __init__() se llama automaticamente cada vez que se usa
#la clase para crear un nuevo objeto

#Metodos de objetos
"""
Los objetos tambien pueden contener metodos. Los  metodos en los objetos
son funciones que pertenecen al objeto.
"""

#Creamos un metodo para la clase persona
class Persona:
    def __init__(Yo, nombre, edad):
        Yo.nombre=nombre
        Yo.edad=edad
        

    def Saludo(Yo):
        print('Hola mi nombre es '+Yo.nombre)
        
        
        
Individuo=Persona('Juan', 59)
Individuo.Saludo()

"""
El parametro 'Yo' es una referencia a la instancia actual de la clase y se usa 
para acceder a las variables que pertenecen a la clase.
"""

#El autoparametro
"""
El parametro self trabajado anteriormente es una referencia a la instancia actual
de la clase y se utiliza para acceder a las variables que pertenecen a la clase.

No tiene que ser nombrado self, puede llamarlo como quiera, pero tiene que ser 
el primer parametro de cualquier funcion de la clase.
"""


class Person:
    def __init__(myobject, name, year):
        myobject.name=name
        myobject.year=year
        
    def My_Fuction(refe):
        print('Hello my name is '+refe.name)
        
person=Person('Juan', 1950)
person.My_Fuction()

#Modificar propiedades de un objeto
person.year=2000

print(person.year)

#Eliminar propiedades de un objeto
#puede eliminar porpiedades en objetos mediante la palabra del
"""
del person.year

print(person.year)
"""
#Eliminar objetos#puede eliminar objetos usando la palabra del

del person

print(person)


#La declaracion pass
"""
Las clases no pueden estar vacias, pero si por alguna razon, la clase
esta sin contenido, la declaracion pass evita un error.
"""
class Cars:
    pass

