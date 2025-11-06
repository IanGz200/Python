class Alertas:
    """
    Classe Alertas, devuelve el color de la arta dependiendo de la temperatura y humedad
    """
    temperatura:int
    humedad:int

    def __init__(self, temperatura:int, humedad:int):
        """
        Constructor
        :param temperatura:
        :param humedad:
        """
        self.temperatura = temperatura
        self.humedad = humedad

    def color(self) -> str:
        """
        Compara la temperatura y humedad para devolver una alerta acorde
        :return: string con la alerta
        """
        color:str
        if self.temperatura > 24 and self.humedad > 50:
            return "Alerta vermella"
        elif self.temperatura > 24 or self.humedad > 50:
            return "Alerta Amarela"
        else:
            return "Alerta verde"

def main():
    """
    Main function
    :return: alerta por pantalla
    """
    alerta = Alertas(int(input("Temperatura: ")), int(input("Humedad: ")))

    print(alerta.color())

if __name__ == "__main__":
    main()