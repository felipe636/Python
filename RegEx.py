#Python RegEx
"""
Un RegEx, o expresion regular, es una secuencia
de caracteres que forma un patron de busqueda.

RegEx se puede usar para verificar si una cadena
contiene el patron de busqueda especificado.
"""

#Modulo RegEx
"""
Python tiene un paquete incorporado llamado 're',
que se puede usar para trabajar con expresiones
regulares.
"""

import camelcase

c= camelcase.CamelCase()

txt='hola'

print(c.hump(txt))
