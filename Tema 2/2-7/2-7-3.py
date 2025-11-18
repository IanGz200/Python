"""
Programa que calcula la suma de los multiplos de 5 entre un minimo y un maximo
"""
minimo:int = 26
maximo:int = 20
resultado:int = 0

"""
En caso de error al ser el minimo mayor al maximo los intercambia
"""
if minimo > maximo:
    print(f"minimo: {minimo} es mayor a maximo: {maximo}")
    temp = minimo
    minimo = maximo
    maximo = temp


for i in range(minimo+1,maximo):
    if i % 5 == 0:
        resultado+=i

print(resultado)

