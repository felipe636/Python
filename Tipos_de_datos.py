#TIPOS DE DATOS EN PYTHON

"""
#Tipo de dato entero
Numero=1998
print(type(Numero))
"""
"""
#Tipo de dato cadena
Nombre='Felipe'
print(type(Nombre))
"""
"""
#Tipo de dato real
Decimal=16.14
print(type(Decimal))
"""

"""
#Tipo de dato complejo
Complejo=6j
print(type(Complejo))
"""

"""
#Tipo de dato Lista
Lista=['Software','Programacion','Algoritmos'] #Las lista van encerradas con llaves cuadradas
print(type(Lista))
"""

"""
#Tipo de dato tupla
Tupla=('Software','Programacion','Algoritmos')#Las tuplas van encerradas con parentesis
print(type(Tupla))
"""
"""
#Tipo de dato rango
Rango=range(7)
print(type(Rango))
"""

"""
#Tipo de dato diccionario
Diccionario={"Nombre":"Felipe","Edad":21,"Apellido":"Zafra"}
print(type(Diccionario))
"""

"""
#Tipo de dato Booleano
Logica=True
print(type(Logica))
"""

#NUMEROS EN PYTHON 
"""
Hay tres tipos de numeros que se trabajan en pyhton
*Entero
*Flotante
*Complejo
"""
"""
Entero=676745 #Los numeros enteros son cualquier entero positivo o negativo
Flotante=556.454
Flot=451e10 #En los numeros complejos se manejan notacion cientifica
Complejo=4j

print(type(Entero))
print(type(Flotante))
print(type(Flot))
print(type(Complejo))
"""

"""
#conversion de tipos de datos numericos
Entero=676745 
Flotante=556.454
flot=455e8
ConversionE=float(Entero)
ConversionF=complex(Flotante)
conversionC=int(flot)
print(ConversionE)
print(ConversionF)
print(conversionC)
print(type(ConversionE))
print(type(ConversionF))
print(type(conversionC))
"""

#NUMEROS ALEATORTIOS 
"""
import random #Modulo de pyhton para generar numeros aleatorios
print(random.randrange(1,20))
"""
"""
#en programacion la conversion entre variables primitivas se llama "Casteo"
Numero=45
Numero2=str(Numero)
print("Un numero entero es: "+Numero2)
"""

#Cadenas en python

Texto="""La programacion es una herramienta poderosa que permite a las
personas solucionar problemas o situaciones del mundo real mediante 
practicas y programas informaticos con el fin de optimizar los procesos"""
#Las matrices tambien funcionan como matrices de bytes
#print(Texto[1])
#Esto se hace llamar rebanada, quiere decir toma el rango de las posiciones
#print(Texto[1:30])
#Rebanadas a la inversa
#print(Texto[-34:-10])
