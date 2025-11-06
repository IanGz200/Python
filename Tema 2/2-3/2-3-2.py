class ImparMayorCien:
    """
    Clase impar_mayor_cien que contie metodos para evaluar numeros impares y mayor a cien
    """

    numero:int

    def __init__(self,numero:int):
        """
        Constructor ImparMayorCien
        :param numero: numero a comprobar
        """
        self.numero = numero

    def impar(self)->bool:
        """
        Comprobar impar
        :return: resultado condicional
        """
        return self.numero%2!=0

    def mayor_cien(self)->bool:
        """
        Comprobar mayor a cien
        :return: resultado condicional
        """
        return self.numero>100

def main():
    """
    Main que crea una clase con la que comprobar si un numero pasado por pantalla es impar o mayor a cien
    """
    imc = ImparMayorCien(int(input("Introduce un número:")))

    if imc.impar() or imc.mayor_cien():
        print("El número cumple la condición")
    else:
        print("El número no cumple la condición")

if __name__ == "__main__":
    main()