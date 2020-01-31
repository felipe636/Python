"""
Var=3//4

print(Var)
"""

"""
#Operadores aritmeticos
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""

"""
#Operadores de asignacion
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""

"""
#Operadores de comparacion
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""

"""
#Operadores logicos
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""

"""
#Operadores de identidad
#Se utilizan para comparar objetos si son o no son iguales
is 	Returns true if both variables are the same object	x is y	
is not	Returns true if both variables are not the same object	x is not y

Frutas=["Fresa","Banana","Manzana"]
Comida=["Papa", "Tomate", "Mazorca"]
Alimentos=Frutas

print(Alimentos is Frutas)
print(Alimentos is not Comida)
"""

"""
#Operadores de membresia 
#Se usan para  saber si un objeto esta presente o no en un conjunto de datos.

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

Fruits=["Banana", "Apple", "Pear"]

print("Pineapple" in Fruits)
print("Apple" in Fruits)
print("Grape" is not Fruits)
"""

"""
#Operadores bit a bit
#Los operadores bit a bit se utilizan para comparar numeros bit a bit
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""