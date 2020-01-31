#Colecciones en Python (Matrices)
"""
Listas
una lista es una coleccion ordenada y modifcable. En python las listas se escriben entre corchetes
"""
Computer=["mouse","cpu","keyboard"]
print(Computer)

#Acceder a los elementos de la lista
print(Computer[2]) #Accede al elemento de la lista colocando el numero de indice de la lista

print(Computer[-1]) #Indezacion negativa: acceder al elemento de la lista desde el final
print(Computer[-2])

print(Computer[0:3]) #Rango de indices esto quiere decir que el rango en los corchetes mostrara el rango de objetos
#En los rangos de indices la busqueda empieza en el primer numero del rango pero no termina en el ultimo elemento 
#del rango.

print(Computer[:3])#Al omitir el primer elemento del rango comenzara desde el indice 0.
print(Computer[0:])#Al omitir el ultimo elemento del rango terminara en el ultimo indice de la lista
print(Computer[-3:-1])#Rangos negativos, manejan casi la misma logica con los rango positivos sino que en este caso
#comienzan desde el final de la lista.

Computer[2]="Board" #Cambiar elementos de una lista
print(Computer[0:3])

#Recorrer los elementos de una lista 
Computer=["mouse","cpu","keyboard"]
for var in Computer: #Se puede recorrer los elementos de una lista con un ciclo for
    print(var)

#Para comprobar si  un objeto existe en una lista se utiliza la palabra clave 'in'
Computer=["mouse","cpu","keyboard"]
if "Webcam" in Computer:
    print('Yes, this object is in this list.')
else:
   print('No, this object is not in this list.')

#Para saber la longitud de la lista se utiliza el metodo len()
   Computer=["mouse","cpu","keyboard","Screen or Monitor"]
   print(len(Computer))

#Para agregar un elemento al final de la lista se utiliza el metodo append()
Computer=["mouse","cpu","keyboard"]
Computer.append("Monitor")
print(Computer)

#Con el metodo insert(), se puede agregar un elemento a la lista con el indice especifico
#Para agregar un elemento al final de la lista se utiliza el metodo append()
Computer=["mouse","cpu","keyboard"]
Computer.insert(1,"Printer")
print(Computer)

#Metodos para eliminar elementos de una lista

#Metodo remove(), elimina un elemento especifico de la lista
Computer=["mouse","cpu","keyboard"]
Computer.remove("mouse")
print(Computer)

#Metodo pop(), elimina un elemento especifico de la lista o en defecto el ultimo elemento de la lista
Computer=["mouse","cpu","keyboard"]
Computer.pop(1)
print(Computer)

#Con la palabra del elimina el elemento que se encuentre en el indice de la fila
Computer=["mouse","cpu","keyboard"]
del Computer[2]
print(Computer)
