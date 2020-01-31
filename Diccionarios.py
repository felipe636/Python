"""
  Diccionarios:
            Un diccionario es una colecccion desordenada, modificable e indexada.
            En python, los diccionarios se escriben entre llaves y tienen claves
            y valores.
"""

#Crear un diccionario

Datos={
    "Año":2020,
    "Mes":"Enero",
    "Edad":21
    }
print(Datos)

#Se puede acceder a los elementos de un diccioario haciendo referencia al nombre
#de la clave  entre corchetes

Acceso=Datos["Edad"]
print(Acceso)


#Existe tambien un metodo llamado get() que le dara el mismo resultado
Acceso=Datos.get("Año")
print(Acceso)

#Puede cambiar valores de un elemento especifico haciendo referencia a su nombre
#de clave

#Cambiar el año a 2030
Datos={
    "Año":2020,
    "Mes":"Enero",
    "Edad":21
    }

Datos["Año"]=2030
print(Datos)

#Recorriendo un diccionario
#puede recorrer un diccionario utilizando un bucle for
"""
Al recorrer un diccionario, el valor de retorno son las claves del diccionario, pero
tambien hay metodos para devolver los valores.
"""
#En este caso imprime todas las claves del diccionario Datos
for i in Datos:
    print(i)

#Una forma de recorrer el diccionario e imprimir susu valores es devolver como un vector
for i in Datos:
    print(Datos[i])

#Tambien se puede utilizar la funcion values() para devolver los valores en un
#diccionario.
for i in Datos.values():
    print("Los valores son",i)

#Para recorrer tanto los valores como las claves de un diccionario se utiliza
#la funcion items()

for i,j in Datos.items():
    print(i,j)

#Comprobar si una clave existe
#Para comprobar si una clave especifica esta en un diccionario use la palabra
#clave in.
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
       }
if "Apeelido" in Datos:
    print('La clave existe en el diccionario Datos')
else:
    print('La clave no existe en el diccionario datos')

#Longitud de un diccionario
"""
Para determinar cuantos elementos (pares clave-valor) tiene un diccionario, use el
len() metodo
"""
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
       }
print(len(Datos))


#Agregar elementos
"""
La adicion de un elemento al diccionario se realiza utilizando una nueva clave
de indice y asignandole un valor:
"""
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
       }
Datos["Pais"]="Colombia"
print(Datos)

#Eliminar elementos
#Existen varios metodos para eliminar elementos de un diccionario

#El metodo pop() elimina el elemento con el nombre de clave especifico
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
       }
Datos.pop("Año")
print(Datos)


#El  metodo popitem() elimina el ultimo elemento insertado(En versiones anteriores
# a python 3.7 elimina un elemento aleatorio)
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
       }
Datos.popitem()
print(Datos)


#La palabra clave del elimina el elemento con el nombre de la clave especifico
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    }
del Datos["Año"]
print(Datos)

#La palabra del tambien puede eliminar el diccionario completo
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    }
"""
del Datos
print(Datos) #Aqui el diccionario se elimina y por lo tanto saldra error en la salida.
"""


#Vaciar un diccionario

#Para limpiar o vaciar un dicccionario se utiliza el metodo clear()
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    }
Datos.clear()
print(Datos)

#Copiar un diccionario

#Una forma de hacer una copia de un diccionario a otro es mediante el metodo copy()
Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    }
Datos2=Datos.copy()
print(Datos2)

#Otra forma de hacer una copia es usar el metodo incorporado dict()

Datos={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    }
Datos2= dict(Datos)
print(Datos2)

#Diccionarios anidados
"""
Un diccionario tambien puede contener muchos diccionarios, esto se llama diccionarios
anidados.
"""

Datos={
     "Fecha":{
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    },
     "Lugar":{
       "Ciudad":"Bucaramanga",
       "Departamento":"Santander",
       "Pais":"Colombia"
    }
}
print(Datos)


#Otra forma de anidar diccionarios es anidar diccionarios que ya existen


Fecha={
       "Año":2020,
       "Mes":"Enero",
       "Edad":21
    }
Lugar={
       "Ciudad":"Bucaramanga",
       "Departamento":"Santander",
       "Pais":"Colombia"
    }

Datos={   #En este diccionario se almacenan los diccionarios ya existentes
     "Fecha":Fecha,  #Se realiza una referencia del diccionario creado.
     "Lugar":Lugar
    }
print(Datos)

#Se puede crear un diccionario con el constructor dict()
Datos=dict(Año=2020, Mes="Enero", Edad=21)
print(Datos)

"""
Métodos de diccionario
Python tiene un conjunto de métodos integrados que puede usar en los diccionarios.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
