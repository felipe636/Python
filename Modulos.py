#Modulos en python
"""
Considere que un modulo es lo mismo que una biblioteca de códigos.

Un archivo que contiene un conjunto de funciones que desea incluir en su
aplicacion.
"""

#Crear un modulo
"""
Para crear un modulo simplemente guarde el codigo que desea en un archivo con
la extension de archivo .py
"""

import mymodule

mymodule.greeting("Jesus") #Cuando use la funcion de un modulo, use la sintaxis
                           #moulo.nombredelafuncion.nombre

#Variables en un modulo
"""
El modulo puede contener funciones, como ya se describio, pero también variables
de todo tipo (matrices, diccionarios, objetos, etc).
"""

import mymodule

person1=mymodule.Person["Age"]
print(person1)


#Nombre un modulo
"""
Puede nombrar el archivo del modulo como desee, pero debe tener la extension de
archivo .py
"""

#Cambiar el nombre de un modulo
"""
Puede crear un alias cuando importe un módulo, utilizando la palabra clave
'as'
"""

#Crea un alias para el modulo 'mymodule' llamado 'mx'
import mymodule as mx

person1=mx.Person["Age"]
print(person1)

#Modulos incorporados
"""
Hay varios módulos integrados en python, que puede importar cuando lo desee.
"""

#importar y usar el modulo platform
import platform

infor=platform.system()
print(infor)

#Usando la funcion dir()
"""
Hay una funcion incorporada para enumerar todos los nombres de funciones (o nombres
de variables) en un modulo. La funcion dir()
"""

import platform

var=dir(platform)
print(var)


#Importar desde modulo
"""
Puede elegir importar solo partes de un módulo utilizando la palabra clave
'from'
"""
from mymodule import Person #Al usar la palabra clave from ya no utiliza en la
                            #la salida la plabra mymodule
print(Person["Name"])


#Como mostrar todas las variables y nombres de funciones de un modulo
import mymodule

print(dir(mymodule))
