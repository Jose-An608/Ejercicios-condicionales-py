'''' Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir '''

saldo = 1000

print ("1. Ingresar dinero en la cuenta. ")
print ("2. Retirar dinero de la cuenta. ")
print ("3. Mostrar dinero disponible. ")
print ("4. Salir. ")
opcion = int (input("Indíque un número del menú: "))

if opcion == 1:
    n = float ( input ("Cuanto dinero vas a ingresar: "))
    saldo = saldo + n

    print ("El dinero en la cuenta es de ",saldo, " ")

elif opcion == 2:
    retirar = float ( input ("Cuanto deseas retirar en la cuenta: "))
    if retirar > saldo:
        print ("No tiene ese saldo disponible")
    else:
        saldo = saldo - retirar
        print ("En la cuenta le queda ",saldo, " ")
elif opcion == 3:
    print ("Su dinero actual es ",saldo, " ")
elif opcion == 4:
    print ("Saliendo...")

else:
    print ("Opcion incorrecta ingresada") 