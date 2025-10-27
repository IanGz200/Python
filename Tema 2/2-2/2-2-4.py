class Pine:
    """
    Clase para crear pinos de una altura determinada y con metodos para modificarla
    """
    def __init__(self, height:float):
        """
        Constructor
        :param height: altura del pino
        """
        self.height:float = height

    def cut(self,cut:float):
        """
        Resta altura del pino
        :param cut: El valor a restar del pino
        """
        self.height = self.height-cut

def main():
    """
    Crea dos pinos de distintas alturas y los acorta con un metodo de clase
    :return: El valor de los pinos antes y despues de cortarlos por pantalla
    """
    p1 = Pine(34)
    p2 = Pine(25)
    print("Arbol 1 entero: ",p1.height)
    print("Arbol 2 entero: ",p2.height)
    p1.cut(7)
    p2.cut(12)
    print("Arbol 1 cortado: ",p1.height)
    print("Arbol 2 cortado: ",p2.height)

if __name__ == '__main__':
    main()