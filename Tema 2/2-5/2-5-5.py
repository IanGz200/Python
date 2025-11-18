"""
Programa que amose por pantalla os dez primeiros números impares.
"""
num:int = 1
cont:int = 0

while cont<10:

    if num % 2 != 0:
        print(num)
        cont+=1

    num+= 1