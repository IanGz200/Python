"""
Programa que calcula la suma de los multiplos de 5 entre un minimo y un maximo
"""
minimo:int = 21
maximo:int = 20
resultado:int = 0

"""
En caso de que el minimo sea mayor a maximo da un error
"""
if minimo > maximo:
    print(f"minimo: {minimo} es mayor a maximo: {maximo}")
else:
    for i in range(minimo+1,maximo):
        if i % 5 == 0:
            resultado+=i

    print(resultado)

