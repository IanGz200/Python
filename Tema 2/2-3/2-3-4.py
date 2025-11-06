class Ascensor:
    """
    Clase Ascensor que realiza una accon dependiendo del valor de una tecla
    """
    accion:str

    def __init__(self, accion):
        """
        Constructor de Ascensor
        :param accion: tecla pulsada por pantalla
        """
        self.accion = accion.lower()

    def tecla(self)->str:
        """
        Metodo que comprueba la tecla pulsada por pantalla
        :return: accion realizada
        """
        match self.accion:
            case "a":
                return "Abriendo puertas"
            case "b":
                return "Bajando"
            case "p":
                return "Cerrando puertas"
            case "s":
                return "Subiendo"
            case _:
                return "Tecla no válida"

def main():
    """
    Main function
    :return: Accion realizada por pantalla
    """
    ascensor = Ascensor(input("Ingresa accion: "))
    print(ascensor.tecla())

if __name__ == "__main__":
    main()