"""
Programa que calcula la suma de los multiplos de 5 entre un minimo y un maximo
"""
minimo:int = 3
maximo:int = 20
resultado:int = 0
for i in range(minimo+1,maximo):
    if i % 5 == 0:
        resultado+=i

    print(resultado)

