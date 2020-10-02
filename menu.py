import os


def Temperaturas():
    print("--- Opción de Temperaturas ---")
    veces = int(input("Cuantas temperaturas ingresa ?: "))
    suma = 0
    for x in range(veces):
        tempe = float(input("Ingrese temperatura: "))
        suma = suma+tempe
    print("El promedio de las temperaturas es: ", round((suma/veces), 2))
    tecla = input("Presione una tecla para continuar")


def Personas():
    print("--- Opción de Datos de Personas ---")
    n = int(input('Cuantas personas ingresa?: '))
    mayor = 0
    menor = 0
    for i in range(n):
        nom = str(input('Ingrese nombre: '))
        edad = int(input('Ingrese edad: '))
        if edad < 18:
            menor = menor + 1
        else:
            mayor = mayor + 1
    print('La cantidad de personas mayores de edad es: '+str(mayor))
    print('La cantidad de personas menores de edad es: '+str(menor))
    tecla = input("Presione una tecla para continuar")
    # ingresar para n personas el nombre y la edad. n debe ser ingresado por teclado
    # mostrar: cuantas personas son mayores de edad y cuantas son menores de edad.
    # subir un tercer commit a git con el mensaje "Se agregó la opción dos al menú"


seguir = True
while seguir:
    os.system('cls')
    print("1. Temperaturas")
    print("2. Datos de Personas")
    print("3. Salir ")
    op = int(input("Ingrese opción 1,2,3: "))
    if(op == 1):
        Temperaturas()  # invocamos a una función
    if(op == 2):
        Personas()  # invocamos a una función
    if(op == 3):
        print("Programa Finalizado")
        break
