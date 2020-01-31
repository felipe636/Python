"""
#LONGITUD DE UNA CADENA
Nombre="Juan Felipe"
print(len(Nombre))
"""
"""
#El metodo strip() elimina los espacios en blanco en el principio o final de una cadena
Nombre="      Juan Felipe Zafra Hernandez     "
print(Nombre.strip())
"""

"""
#El metodo lower() devuelve todo el contenido de la cadena en minusculas
Cadena="Desarrollo de software Al Maximo"
print(Cadena.lower())
"""

"""
#El metodo upper() devuelve el contenido de la cadena en  mayusculas
Cadena="Desarrollo de software es lo Maximo"
print(Cadena.upper())
"""

"""
#El metodo replace reemplaza una cadena con otra
Cadena="Hola soy Felipe"
print(Cadena.replace('s','j'))
"""

"""
#El metodo split() divide una cadena en subcadenas si encuentra instancias separadas
Cadena="Hola soy Felipe"
print(Cadena.split())
"""

"""
#Cadenas de verificacion
#para verificar si una frase o caracter esta presente en una 
#cadena se utiliza las palabras claves 'in', 'not in'

Cadena="Hola soy Felipe"
Palabra='Estoy' in Cadena
print(Palabra)

Cadena="Hola soy Felipe"
Palabra='Estoy' not in Cadena
print(Palabra)
"""

"""
#Concatenacion de cadenas
#Para concatenar dos o mas cadenas se usa el operador +

Nombre='Juan'
Edad='21'
Informacion= Nombre +" "+ Edad
print(Informacion)
"""
"""
 #Formato de cadena
#Se utiliza el metodo format() para formatear una cadena y 
#agregar un valor numerico donde este el signo {}
Name='I am Felipe, and I am {} years old'
Age=21
print(Name.format(Age))


year = 2020
dolar = 3500
myorder = "In the year {} the dolar in Colombia is in {} colombia money"
print(myorder.format(year, dolar))
"""


#Caracter de escape '\', se utiliza para colocar un caracter 
#entre comillas en una cadena, cuando se muestra en la salida

Text="The software is \"Amaizing\" in the life."
print(Text)