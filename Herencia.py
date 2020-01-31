#Herencia de python
"""
La herencia nos permite definir una clase que hereda todos los métodos
y propiedades de otra clgateoase. La clase padre es la clase de la que se
hereda, también llamada clase base. La clase secundaria es la clase
que hereda de otra clase, también llamada clase derivada.
"""

#Cualquier puede ser una clase principal, por lo que la sintaxis es la misma
#que crear cualquier otra clase.

class Person:
    def __init__(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print(self.firstname, self.lastname)

#Crear un metodo y utilizar el metodo printname
_object=Person("Juan", "Zafra")
_object.printname()


#Crear una clase Hija
"""
Para  crear una clase que herede la funcionalidad de otra clase, envie la clase
primaria como parametro al crear la clase secundaria.
"""

#Crear una clase llamada 'Student', que hereda las propiedades y métodos de la
#la clase Person.

class Student(Person):
    pass
_object2=Student("Bill","Smith")
_object2.printname()

#Agregue la funcion __init__()
"""
Hasta este momento se ha creado una clase secundaria que hereda las propiedades
y métodos de su padre.
Queremos agregar la funcion __init__() a la clase secundaria (En lugar de la
palabra clave pass).

La funcion __init__() se llama automaticamente cada vez que se usa la clase
para crear un nuevo objeto.

Cuando agrega la funcion __init__() a la clase secundaria, ya no heredara de la
funcion principal __init__().

Es decir anula la herencia de la clase Padre.

Para mantener la herencia de la función del padre __init__()  , agregue una
llamada a la función del padre __init__() :
"""

#Ejemplo donde se agrega la funcion __init__() a la clase Student
class Student(Person):
    def __init__(self,firstname,lastname):
        Person.__init__(self,firstname, lastname) #Llamada de a la funcion de la clase padre.
            
my_student=Student("Amanda","Ruiz")
my_student.printname()

"""
Ahora hemos agregado con éxito la función __init __ (), y hemos mantenido la
herencia de la clase padre, y estamos listos para agregar funcionalidad en
la funcion __init__().
"""

#Utilizando la funcion super()
"""
Python tambien tiene una funcion llamada 'super()' que hará que la clase hija
heredo todos los metodos y propiedades de la clase padre.
"""
class Student(Person):
    def __init__(self,firstname,lastname):
        super().__init__(firstname, lastname)

my_student2=Student("Megan","Fox")
my_student2.printname()

#Agregando propiedades a la clase hija

#Agregar una propiedad llamada graduationyear(Año de graduacion) a la clase
#Student
class Student(Person):
    def __init__(self,firstname,lastname):
        super().__init__(firstname, lastname)
        self.graduationyear=2019
        
my_student2=Student("Megan","Fox")
print(my_student2.graduationyear)

"""
Agregue un parametro 'year' y pase el año al crear objetos
"""
class Student(Person):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname, lastname)
        self.graduationyear=year
        
my_student2=Student("Megan","Fox",2030)
print(my_student2.graduationyear)

#Agregar metodos
"""
En este ejemplo se agregara un metodo llamado 'Bienvenido'
"""
class Student(Person):
     def __init__(self,firstname,lastname,year):
        super().__init__(firstname, lastname)
        self.graduationyear=year

     def welcome(self): 
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

the_student=Student('Margarita','Zafra',2046)
the_student.welcome()
    

"""
Si agrega un método en la clase secundaria con el mismo nombre que una función
en la clase primaria, se anulará la herencia del método primario.
"""










    
