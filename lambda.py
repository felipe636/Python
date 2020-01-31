#Python Lambda
"""
Una funcion Lambda es una pequeña funcion anonima.
Una funcion Lambda puede tomar cualquier número de argumentos, pero solo puede
tener una expresion.
"""

#lambda arguments:expression #Esta es la sintaxis de una expresion lamda   

x=lambda a:a+10
print(x(5))

#Las funciones de Lambda pueden tomar cualquier número de argumentos.
#Ejemplo de una funcion Lambda

Resul=lambda Num1, Num2:Num1*Num2
print(Resul(8,4))

Suma=lambda Num1,Num2,Num3: Num1+Num2+Num3
print(Suma(7,84,11))

"""
¿Por qué usar funciones lambda?

El poder de lambda se muestra cuando los usa como una función anónima dentro de otra funcion.
Supongamos que tiene una definicion de funcion que toma un argumento, y ese argumento se
multiplicara con un número desconocido:
"""

#Use una funcion lambda para hacer que una funcion siempre duplique el numero que envia como 
#argumento.

def  Duplicar(Num):
    return lambda Dupli:Dupli*Num
    
Num_Dupli =Duplicar(2)


print(Num_Dupli(50))
