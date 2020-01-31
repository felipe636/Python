#Fechas en python
"""
Una fecha en python no es un tipo de datos, pero podemos importar un modulo
nombrado datatime para trabajar con fechas como objetos de fecha.
"""

#Importe el modulo de fecha y muestre la hora actual

import datetime

Hour=datetime.datetime.now()
print(Hour)

#Fecha de salida
"""
Cuando ejecutamos el codigo del ejemplo anterior, el resultado será la hora actual.

La fecha contiene año, mes, hora, minuto, segundo y microsegundo.

El modulo 'datetime' tiene muchos metodos para devolver informacion sobre el
objeto de fecha.

"""

#Retornar el año y el nombre del dia de la semana

import datetime

var=datetime.datetime.now()

print(var.year)
print(var.day)
print(var.strftime('%A'))

#Crear objetos de fecha
"""
Para crear una fecha, podemos usar la clase(constructor) datetime() del
modulo datetime().

La clase datetime() requiere tres parametros para crear una fecha: año, mes, dia.
"""

import datetime

var=datetime.datetime(2020,12,31)

print(var)


"""
La datetime()clase también toma parámetros para hora y zona horaria
(hora, minuto, segundo, microsegundo, tzone), pero son opcionales y
tiene un valor predeterminado de 0, ( Nonepara zona horaria).
"""

#El metodo strftime()
"""
El objeto datetime tiene un metodo para formatear objetos de fecha en cadenas
legibles.

El metodo se llama strftime() y toma un parametro format para especificar el
formato de la cadena devuelta.
"""

import datetime

var=datetime.datetime(2020,12,31)

print(var.strftime('%B'))

"""
Una referencia de todos los códigos de formato legal:

Directive	Description	Example	T
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	

"""
