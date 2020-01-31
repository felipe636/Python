"""
#En programacion los valores booleanos devuelven dos valores True o False
print(2==4)
print(4>2)
"""

"""
#En los condicionales las salidas son True or False
if(4>2):
    print('4 es  mayor 2')
else:
   print('4 no es mayor que 2')
"""

"""
#La mayoria de los valores son verdaderos
print(bool('Hola'))
print(bool(23))
"""

"""
#Los valores falsos pueden ser por lo siguiente
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""


#Con el metodo isintance() devuelve el estado booleano de una variable inicializada
Var=0
print(isinstance(Var, int))