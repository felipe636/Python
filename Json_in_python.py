#Python json
"""
JSON es una sintaxis para almacenar e intercambiar datos.
JSON es texto, escrito con notacion de objetos de Javascript.
"""

#Json en python
"""
Python tiene un paquete incorporado llamado json, que puede
usarse para trabajar con datos JSON.
"""
import  json

#Parse JSON- convertir de json a python
"""
si tiene una cadena JSON, puede analizarla utilizando el metodo json.loads().
"""

import json

Datos='{"Nombre":"Jesus","Edad":33,"Ciudad":"Israel"}'

#parseo de la variable Datos
Datos2=json.loads(Datos)

#El resultado es un diccionario de python
print(Datos2["Nombre"])

#Convertir de python a Json
"""
Si tiene un objeto python, puede convertirlo en una cadena JSON utilizando el
metodo json.dumps().
"""

#Convierte de python a Json

import json

#El objeto en este caso un diccionario
Persona={
    "Nombre":"Juan",
    "Edad":33,
    "Ciudad":"Bogota"
    }

#Convertirlo dentro de un Json
Datos=json.dumps(Persona)

print(Datos)

"""
Puede convertir objetos de Python de los siguientes tipos, en cadenas JSON:

dict
lista
tupla
string
int
float
True
False
None
"""

import json

print(json.dumps({'Nombre':'Felipe','Edad':34}))
print(json.dumps('Juan Felipe Zafra'))
print(json.dumps(('computador','televisor')))
print(json.dumps(78))
print(json.dumps(True))
print(json.dumps(None))


"""
Cuando convierte de Python a JSON, los objetos de Python se
convierten en el equivalente de JSON (JavaScript):


Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
"""


#Convierta un objeto python quecontenga todos los tips de datos legales

import json

Datos={
    "Nombre":"Juan",
    "Edad":45,
    "Casado":False,
    "Soltero":True,
    "Hijos":("Margarita","Antonio"),
    "Mascotas": None,
    "Vehiculos":[
        {"modelo":"BMW", "Año":1993},
        {"modelo":"Ford", "Año":2018}
      ]

    }

print(json.dumps(Datos))

#Dar formato al resultado
"""
El ejemplo anterior imprime una cadena JSON, pero
no es muy fácil de leer, sin sangrias ni saltos
de linea.

El metodo json.dumps()  tiene parametros para
facilitar la lectura del resultado.

Uno de los parametros es indent, sirve para definir
el numero de sangrias.
"""

import json

Datos2={
    "Nombre":"Juan",
    "Edad":45,
    "Casado":False,
    "Soltero":True,
    "Hijos":("Margarita","Antonio"),
    "Mascotas": None,
    "Vehiculos":[
        {"modelo":"BMW", "Año":1993},
        {"modelo":"Ford", "Año":2018}
      ]

    }

print(json.dumps(Datos2, indent=4))

"""
También puede definir los separadores, el valor
predeterminado es (",", ":"), lo que significa
usar una coma y un espacio para separar cada
objeto, y dos puntos y un espacio para separar
las claves de los valores
"""

#Ejemplo de separadores
"""
Use el parametro 'separators' para cambiar el
separador predeterminado.
"""
print(json.dumps(Datos, indent=5, separators=(".","=")))

#Ordene el resultado
"""
El metodo jsonn.dumps() tiene parametros para
ordenar las claves en el resultado.

Usa el parametro sort_Keys para especificar si
el resultado  debe ordenarse o no.
"""
print(json.dumps(Datos, indent=4, sort_keys=True))
