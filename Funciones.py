    
#Funciones
"""
Una funcion es un bloque de codigo que solo se ejecuta cuando se llama.
Puede pasar datos, conocidos como parametros, a una funcion.
Una funcion puede devolver datos como resultado.
"""

#En python, una funcion se crea usando la palabra clave 'def'

def Mi_Funcion():
    print('Hola mundo')
    
    
#Para llamar una funcion usa el nombre de la funcion seguido de el parentesis   
Mi_Funcion()


#Argumentos
"""
La informacion  de puede pasar pasar a funciones como argumentos.
Los argumentos se especifican despues del nombre de la funcion, dentro de los 
parentesis. Puede agregar tantos argumentos como desee, simplemente se tiene 
que separar con una coma.
"""

#Ejemplo de una funcion que pasa como argumento el nombre de una persona

def Saludo(nombre):
    print('Hola como estas',nombre)
    
    
Saludo('Juan')
Saludo('Fernanda')

"""
Parametros o argumentos?
Los terminos parametro y argumento pueden usarse para lo mismo: basicamente
es la informacion que se pasa a una función.

Desde la perspectiva de una función:
*Un parametro es la variable listada entre paréntesis en la definicion definicion
de la funcion.
*Un argumento es el valor que se envia a la funcion cuando se llama.
"""

#Numero de argumentos 
"""
Por defecto, se debe llamar a una funcion con el numero correcto debe
de argumentos. LO que significa que si su funcion espera 2 argumentos, debe
llamar a la funcion con 2 argumentos, ni mas ni menos.
"""

def Saludo(Nombre, Apellido):
    print('Su nombre es: ',Nombre)
    print('Su Apellido es: ',Apellido)
    
#El numero de argumentos debe ser igual tanto en entrada como en salida    
Saludo('Juan','Zafra')


#Argumentos arbitrarios, *Argumentos
"""
Si no sabe cuantos argumentos se pasaran a su funcion, agregue un * antes del
nombre del parametro de la definicion de la funcion.

De esta forma, la función recibira una tupla de argumentos y podrá acceder
a los elementos en consecuencia.
"""

def Saludo(*Nombre):
    print('Hola '+Nombre[1])
    
Saludo('Diego','Andres','Felipe')


#Los argumentos  arbitrarios a menudo se acortan a *args en las documentaciones
#de python.


#Argumentos con clave valor

"""
Tambien puede enviar argumentos con la sintaxis clave=valor.
De esta manera, el orden de los argumentos no importa.
"""

def Saludo(Nombre1,Nombre2,Nombre3):
    print('Hola '+Nombre1)

Saludo(Nombre1='Diego', Nombre2='Andres',Nombre3='Felipe')


#Argumentos arbitrarios de palabras clave, **Kwargs
"""
Si no sabe cuantos argumentos de palabras clave se pasaran a su funcion,
agregue dos asteriscos: ** antes del nombre del parametro en la definicion
de la funcion.

De esta forma, la funcion recibirá un diccionario de argumentos y podra
acceder a los elementos en consecuencia:
"""

#Si se desconoce el numero de argumentos ,agregue doble asteriscos
def Gretting(**Name):
    print('Hello '+Name['First'])
    
Gretting(First='Will', Second='Aaron')    
    
#Valor de argumentos predeterminados
"""
El siguiente ejemplo muestra como usar un valor de parametro predeterminado. Si llamamos
a la funcion sin argumento, utiliza el valor predeterminado.
"""

def Cars(Models="Ford"):
    print('The model of the car is: '+Models)
    
Cars("Ferrari")
Cars("BMW")
Cars()
    
#Pasar una lista como argumento
"""
Puede enviar cualquier tipo de argumento de datos a una funcion (cadena, numero, lista,
diccionario, etc.) y se tratara como el mismo tipo de datos dentro de la funcion.

Por ejemplo, si envia una Lista como argumento, seguirá siendo una Lista cuando alcance 
la función.
"""

def Food(Vegetables):
    for i in Vegetables:
        print(i)

Fruits=['Bananas','Grapes','Apples']
Food(Fruits)

#Valores de retorno
"""
Para permitir que una funcion devuelva un valor, use la instruccion
return
"""

def Suma(Num):
    return 10+Num
    
print(Suma(7))
print(Suma(2))
print(Suma(3))

#La declaracion pass
"""
Las definiciones de las funciones no pueden estar vacias, pero si por alguna
razón tiene una funcion sin contenido, ingrese la instruccion pass evitar
un error.
"""

def Sumar():
    pass

#Recursividad
"""
Python tambien acepta la recursion de funciones, lo que significa que una funcion
definida puede llamarse a si misma.

La recursion es un concepto matematico y de programacion común. Significa qu una 
funcion se llama a si misma. Esto tiene el beneficio de significar que puede recorrer
los datos para llegar a un resultado.

El desarrollador debe tener mucho cuidado con la recursividad, ya que puede ser bastante
fácil escribir una función que nunca termina o una que usa cantidades excesivas de 
memoria o potencia del procesador. Sin embargo, cuando se escribe correctamente,
la recursión puede ser un enfoque de programación muy eficiente y matemáticamente 
elegante.
"""

def Recursividad(Var):
    if(Var>0):
        resultado=Var+Recursividad(Var-1)
        print(resultado)
    else:
        resultado=0
        return resultado
    
print('\n\Los resultados de la recursion son: ')
Recursividad(6)
    
