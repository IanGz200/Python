import math

class Hipotenusa:
    """
    Clase que dados dous catetos (como variables de tipo double) devolva o valor da hipotenusa.
    """
    #Constructor de clase
    def __init__(self,c1:float,c2:float):

        self.cateto1 = c1
        self.cateto2 = c2


    def hipoteusa(self) -> float:
        """
        Metodo que calcula el valor de la hipotenusa.
        :return: hipotenusa de los catetos
        """
        hipotenusa:float = math.sqrt((self.cateto1**2) + (self.cateto2**2))

        return hipotenusa

def main():
    """
    Main que pide dos valores por consola y calcula la hipotenusa de estos con la clase Hipotenusa
    """

    cat1:float = float(input("Ingrese el valor del cateto 1: "))
    cat2:float = float(input("Ingrese el valor del cateto 2: "))

    h = Hipotenusa(cat1,cat2)

    print("La hipotenusa de los catetos",cat1,"y",cat2,"es:",h.hipoteusa())

if __name__ == "__main__":
    main()