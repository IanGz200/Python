"""
Programa que calcula la potencia de un número
"""
numero:int = int(input("Ingresa un numero: "))
potencia:int = int(input("Ingresa la potencia: "))
resultado:int = numero

for i in range(1,potencia):
    resultado*=numero

print(resultado)