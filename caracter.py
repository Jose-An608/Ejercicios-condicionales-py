''' Hacer un programa que pida un carácter e indique si es una vocal o no.'''

m = input("Indique un caracter: ").lower()

if  m == 'a' or m == 'e' or m == 'i' or m == 'o' or m == 'u':
    print(" El caracter es una vocal ")
else:
    print(" No es una vocal ")