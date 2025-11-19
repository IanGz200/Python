
number:int = int(input("Ingresa un numero: "))

def check(num:int)->bool:
    """
    Este metodo comprueba si un numero es divisible por otro entre 3 y el mismo. En caso de poder se determina que no es
    primo por lo que devuelve false
    :param num: numero a comprobar
    :return: Si es o no primo
    """
    for i in range(3,num):
        if num % i == 0:
            return False

    return True


while number > 0:
    if check(number) or number == 2:
        print(number)

    number -=1