import math


class Ecuacion:

    def __init__(self):
        self.a:int = 1
        self.b:int = -2
        self.c:int = -15
        self.sol_p:float = 0
        self.sol_n:float = 0

    def resolver_ecuacion(self) -> tuple[float,float]:
        self.sol_p = (-self.b + math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a
        self.sol_n = (-self.b - math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a

        return self.sol_p, self.sol_n

def main():

    ecu = Ecuacion()

    i:int = 0
    while i < len(ecu.resolver_ecuacion()):
        print(ecu.resolver_ecuacion()[i])
        i+=1
        if i == len(ecu.resolver_ecuacion())-1:
            print("y")


if __name__ == '__main__':
    main()