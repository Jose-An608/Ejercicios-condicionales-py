''''Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones
aritméticas básicas (suma, resta, multiplicación y división). El usuario debe especificar la operación con el primer carácter  del nombre de la operación.
S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División'''

m = float (input ("De el primer número: "))
n = float (input ("De el segundo número: "))

print (" ")

print ("Escoga el primer caracter de la operacion que desea hacer: ")

print ("S.s - Suma")
print ("R,r - Resta")
print ("P,p,M,m - Multiplicación")
print ("D,d - División")

print ( " ")

x = input (" ").lower()
if  x  == 's' :
    s = m + n
    print ( "La suma es: ",s, " ")
elif x == 'r' :
    r = m - n
    print ( "La resta es: ", r, " ")
elif x == 'p' or 'm':
    mul = m * n
    print ( "La multiplicación es: ", mul, " ")
elif x == 'd':
    d = m/n
    print ( "La división es: ", d, " ")
