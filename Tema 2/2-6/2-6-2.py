"""
Programa que calcula el resultado de sumar un "numero" "numero2" veces
"""
numero1:int = 5
numero2:int = 4
resultado:int = numero1

for i in range(1,numero2):
    resultado+=numero1

print(resultado)