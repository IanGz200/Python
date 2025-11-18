"""
Programa que pide un numero por pantalla y te dice si es primo o no, sigue pidiendo hasta que se inserte un 0
"""

numero = int(input("Ingresa un numero: "))

while numero!=0:
    primo = True
    """
    En caso de que sea divisible por un numero distinto a si mismo o 1 no es primo
    """
    for i in range(2,numero):
        if numero%i==0:
            primo = False

    if primo:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

    numero = int(input("Ingresa un numero: "))