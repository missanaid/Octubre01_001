# Ingresar dos numeros como int
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
# operadores matematicas
suma = a+b
multi = a*b
print("La suma de " + str(a) + " con el numero " +
      str(b) + "es igual a: "+str(suma))
print("La multiplicacion de " + str(a) +
      " con el numero "+str(b) + " es igual a: "+str(multi))

if a > b:
    print("El numero "+str(a) + " es mayor que "+str(b))
elif a < b:
    print("El numero "+str(b) + " es mayor que "+str(b))
else:
    print("Los numeros son iguales")
