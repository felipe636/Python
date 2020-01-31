
"""
Condicionales:
  Los condicionales son estructuras de decision que permiten evaluar el estado
  logico de una condicion y posterior a la evaluacion se ejecutan las instrucciones
  logicas.

Python admite las condiciones lógicas habituales de las matemáticas:

Igual: a == b
No es igual: a! = B
Menos de: a <b
Menor o igual que: a <= b
Mayor que: a> b
Mayor o igual que: a> = b
"""

#Se escribe una declaracion si, utilizando la palabra clave 'if'

var1=23
var2=34
if var1>var2:
    print(var1,' es mas grande que',var2)
else:
    print(var1,' No es mayor que', var2)


#Sangrias en python
"""
Python se basa en la sangría (espacio en blanco al comienzo de una línea)
para definir el alcance en el código. Otros lenguajes de programación a
menudo usan llaves para este propósito.
"""
"""
#este codigo generara un error porque no utiliza sangria
var1=23
var2=34
if var1>var2:
print(var1,' es mas grande que',var2)
else:
print(var1,' No es mayor que', var2)
"""

#Elif
"""
La palabra 'elif' es la forma de decir que si las condiciones anteriores no son
ciertas entonces intente con esta condicion.
"""
#Programa para evaluar el mayor de dos numeros
Var1=int(input('Digite un numero entero: '))
Var2=int(input('Digite un numero entero: '))
if Var1>Var2:
    print(Var1,' es mayor que ', Var2)
elif Var2>Var1:
    print(Var2,' es mayor que ', Var1)
elif Var1==Var2:
    print('Los dos numeros son iguales')

#La condicion 'else' ejecuta la condicion si las anteriores no son verdaderas
    #Programa para evaluar el mayor de dos numeros
VarA=5.3
VarB=5.3
if VarA>VarB:
    print(Vara,' es mayor que ', Varb)
elif VarB>VarA:
    print('Los dos numeros son iguales')
else:
    print('Los dos numeros son iguales')

#si solo tiene una  instruccion puede ponerla en una sola linea
VarC=7
VarD=5
if VarC>VarD: print(VarC,' es mayor que ',VarD)

#Si solo tiene que ejecutar una instruccion, uaa para if y otra para else, puede
#ejecutar en  la misma linea
VarV=1
VarX=2
print(VarV) if VarV>VarX else print(VarX)

#Tambien puede utilizar varias instrucciones en una misma linea
Var_1=76
Var_2=76
print("A") if Var_1>Var_2 else print("=") if Var_1==Var_2 else print("B")

#Tambien se puede utilizar operadores logicos para relacionar condicionales

#En este ejemplo se trabajara con el operador logico and
Num1=785785
Num2=646
Num3=6465
if Num1>Num2 and Num1>Num3:
    print('Ambas condiciones son verdaderas')

#En este ejemplo se trabajara con el operador logico or
Num_1=785785
Num_2=646
Num_3=6465

if Num1>Num2 or Num1<Num3:
    print('Una de las condiciones es verdadera')

#Desiciones anidadas
"""
Las decisiones anidadas estan constituidas por declaraciones internas.
"""
Numero=1998
if Numero>100:
   print(Numero,'Es mas grande que 100')
   if Numero>200:
      print(Numero,'Es mas grande que 200')
else:
    print('El numero no es mas grande que 200')

#La declaracion 'pass'
"""
La declaracion pass, se utiliza en sentencias condicionales vacias con el fin
de que no generen un error.
"""

Number=13
Number2=45

if Number<Number2:
    pass



