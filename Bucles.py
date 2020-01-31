"""
Bucles en python:
  Los bucles son sentencias ciclicas en programacion en. En python hay dos
  comandos primitivos.

  *Ciclo mientras(while)
  *Ciclo Para (For)
"""

#Bucle while
print("CICLOS MIENTRAS")
"""
Con el ciclo while podemos ejecutar un conjunto de instrucciones siempre y cuando
se cumpla la condicion.
"""

Numero=23 #En este caso necesitamos una variable de idexacion para trabajar el  bucle.
while Numero<50:
    print(Numero)
    Numero +=1

#Recuerde que por sintaxis del lenguaje se trabaja con identacion.


#La instruccion 'break' es utilizada para romper o parar una condicion de un bucle.
Numero=1
while Numero<10:
    print(Numero)
    if Numero==5:
       break
    Numero +=1

#Con la sentencia 'continue' podemos detener la iteracion actual y continuar con
#la siguiente es decir saltar la condicion interna.
Numero=1
while Numero<10:
    Numero +=1
    if Numero==5:
       continue
    print(Numero)

#Con la instruccion else podemos ejecutar un bloque de codigo cuando la condicion
#ya no es verdadera.

Numero=1
while Numero<=10:
    print('El numero de la serie es: ',Numero)
    Numero +=1
else:
   print('La serie no debe que ser mayor que 10')


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
    

