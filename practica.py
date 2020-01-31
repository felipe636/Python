"""
Bucle para:
  un bucle for se usa para iterar sobre una secuencia(que es una lista, una tupla, un diccionario, un conjunto
  o una cadena).
  
  Basicamente funciona como un iterador.
  """
  
  #Imprimir cada elemento de la  siguiente lista
Dispositivos=["Televisor", "Computador", "Lavadora"]
for i in Dispositivos:
    print(i)
    
  #Bucles a traves de una cadena, las cadenas son objetos iterables, contiene una secuencia de caracteres
  """
for i in "Juan Felipe":
    print(i)
"""

#La declaracion break
#Con esta declaracion se puede detener un ciclo antes de que haya 
#pasado por todos los elementos.
Dispositivos=["Televisor", "Computador", "Lavadora"]
for i in Dispositivos:
    print(i)
    if i=="Computador":
        break

#En este caso el break se da antes de la impresion
Dispositivos=["Televisor", "Computador", "Lavadora"]
for i in Dispositivos:
    if i=="Computador":
        break
    print(i)
    
#con la declaracion continue ignora al elemento señalado
Dispositivos=["Televisor", "Computador", "Lavadora"]
for i in Dispositivos:
    if i=="Computador":
        continue
    print(i)
    
#La funcion range() permite recorrer un numero especifico de veces
Num=int(input('Digite un numero entero: '))

for i in range(1,Num):  #De esta manera se especifica desde donde comienza el ciclo
    print('La secuencia de numeros= ',i)
    
#Para incrementar los valores en un ciclo for 
for i in range(1,20,2): #El ultimo numero especifica el incremento
    print(i)
    
#La palabra else especifica una linea de codigo que se ejecuta al terminar
#la ejecucion del Bucle
for i in range(1,10):
    print(i)
else:
    print('Bucle finalizado')
    
#Bucles anidados 
"""
Un bucle anidado es un bucle dentro de un bucle.
El "bucle interno" se ejecutara una vez cada iteracion del bucle
"externo"
"""
Dispositivos=["Televisor", "Computador", "Lavadora"]
Comida=['Cereal','Arroz','Lentejas']
for i in Dispositivos:
    for j in Comida:
        print(i,j)
    
#La declaracion 'pass'
for i in [1,2,3]:
    pass
    
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

#Arrays in Python
"""
Python no tiene soporte integrado para matrices, pero las listas de python se 
pueden usar en su lugar.
"""

#matrices
"""
Las matrices se utilizan para almacenar multiples valores en una sola varible
"""

#Crear una matriz que contenga nombres de automoviles
Carros=["BMW","Ferrari","Ford"]
print(Carros[0])

"""
Una matriz es una variable especial, que puede contener mas de una valor a la vez.
Para acceder a los valores de una matriz se hace la referencia con el 
numero de indice.
"""

#Modificando el valor de la posicion  de la matriz
Carros[0]='Hunday'
print(Carros)

#La longitud de una matriz

"""
Para devolver la longitud de una  matriz( el numero de elementos de una}
matriz) se utiliza el metodo len()
"""
Cars=len(Carros)
print(Cars)

#Recorrer una matriz con un bucle For
"""
Puede usar el bucle for in para recorrer todos los elementos de una 
matriz.
"""
for i in Carros:
    print(i)
    
#Agregar elementos a una matriz
"""
Puede usar el metodo append() para agregar elementos a una matriz.
"""

Carros.append("BMW")
print(Carros)

#Eliminar elementos de una matriz 
"""
Puede usar el metodo pop() para eliminar elementos de una matriz
"""

Carros.pop(2)
print(Carros)

#Tambien puede eliminar elementos de una matriz con el metodo remove()

Carros.remove('Hunday')
print(Carros)

"""
Métodos de matriz
Python tiene un conjunto de métodos integrados que puede usar en listas / matrices.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

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






    