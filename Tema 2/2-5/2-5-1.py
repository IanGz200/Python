numero:int = int(input())
cont:int = 1
factorial:int = 1

"""
Bucle que calcula el factorial al multiplicar un numero por un resultado "numero" de veces
"""
while cont <= numero:
    factorial *= cont
    cont+=1

print(factorial)