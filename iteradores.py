#Iteradores en python
"""
Un iterador es un objeto que contiene un número contable de valores.
Un iterador es un objeto sobre el que se puede iterar, lo que significa que
puede atravesar todos los valores.

Tecnicamente, en python, un iterador es un objeto que implementa el protocolo
de iterador, que consiste en los metodos __iter__() y __next__().
"""

#Iterador vs Iterable
"""
Las listas, tuplas, diccionarios y conjuntos son todos objetos iterables. Son
contenedores iterables de los que puede obtener un  iterador.

Todos estos objetos tienen un metodo iter() que se utiliza para obtener un
iterador.
"""

Fruits=("apple","grapes","bananas","pineapples")
iteration=iter(Fruits)

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))


#Incluso las cadenas son objetos iterables y pueden devolver un iterador
MyCadena="JuanFelipe"
IterationStr=iter(MyCadena)

print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
print(next(IterationStr))
      
#Recorriendo un iterador
"""
Tambien podemos usar un ciclo for para iterar a traves de un objeto iterable.
"""
Fruits=("apple","grapes","bananas","pineapples")

for i in Fruits:
    print(i)

#Iterar sobre los elementos de una cadena
MyCadena="JuanFelipe"

for i in MyCadena:
    print(i)

"""
Para crear un objeto/clase como iterador, debe implementar los metodos __iter__()
y __next___()en su objeto.
"""

class Numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
mynumbers=Numbers()
myiter=iter(mynumbers)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#La declaracion StopIteration
"""
Para evitar que la iteracion continue para siempre, podemos usar la
declaracion StopIteration.

En el metodo __next__() podemos agregar una condicion de terminos para generar un
error si la iteracion se realiza u número especifico de veces.
"""
class Numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
      if self.a <=10:
          x=self.a
          self.a+=1
          return x
      else:
          raise StopIteration
        
mynumbers=Numbers()
myiter=iter(mynumbers)

for i in myiter:
    print(i)
