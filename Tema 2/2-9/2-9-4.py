import random

MAX:int = int(input("Introduce un numero maximo:"))
intentos:int = int(input("Introduce el máximo de intentos:"))
value:int = random.randrange(MAX)
finish:bool = False

while not finish:
    """Pide el numero por pantalla"""
    num:int = int(input("Introduce un numero:"))
    """
    En caso de acertar anuncia la victoria y termina el juego.
    Si no se acierta indica si en valor es mayor o menor.
    Si se tienen demasiados fallos anuncia la derrota y termina el juego.
    """
    if num == value:
        print("Has ganado")
        finish = True
    else:
        intentos -= 1
        if intentos == 0:
            print("Has perdido")
            finish = True
        else:
            if num > value:
                print("El numero es menor")
            else:
                print("El numero es mayor")