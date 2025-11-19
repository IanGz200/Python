"""
Bucle anidado que saca una matriz 5*5 por pantalla
"""
number:int = 10
for j in range(1,6):
    number2 = number
    for k in range(1,6):
        print(number2,end=" ")
        number2-= 1
    print()
    number-=1