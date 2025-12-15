import random


class ColorCombination:
    """
    Esta clase implementa unha combinación de cores, que usaremos tanto para a combinación de cores oculta como a
    combinación que introduza o usuario en cada intento que faga.
    """

    colors: list[int]

    RED: int = 0
    GREEN: int = 1
    YELLOW: int = 2
    PINK: int = 3
    NUMBER_OF_COLORS = 4
    COMBINATION_SIZE = 3

    def get_colors_as_string(self) -> str:
        """
        Este metodo devolve un string coa representación da combinación de cores
        :return: combinación de cores
        """

        cores = ""

        for color in self.colors:
            if cores != "":
                cores += " "

            match color:
                case ColorCombination.RED:
                    cores += "vermello"
                case ColorCombination.GREEN:
                    cores += "verde"
                case ColorCombination.YELLOW:
                    cores += "amarelo"
                case ColorCombination.PINK:
                    cores += "rosa"

        return cores

    def generate_combination(self) -> None:
        """
        Este metodo xera una combinacion de cores aleatoria entre 0 e 4
        """

        self.colors = []
        for color in range(ColorCombination.COMBINATION_SIZE):
            cor = random.randrange(ColorCombination.NUMBER_OF_COLORS)
            while cor in self.colors:
                cor = random.randrange(ColorCombination.NUMBER_OF_COLORS)

            self.colors.append(cor)

    def get_hits(self, another_combination: "ColorCombination") -> int:
        """
        Este metodo devolve a cantidad de cores acertados na mesma posicion
        :param another_combination: los colores a comparar
        :return: colores acertados na mesma posicion
        """

        cont = 0

        for i in range(ColorCombination.COMBINATION_SIZE):
            if another_combination.colors[i] == self.colors[i]:
                cont += 1

        return cont

    def get_common_colors(self, another_combination: "ColorCombination") -> int:
        """
        Este metodo devolve a cantidad de cores acertados
        :param another_combination: los colores a comparar
        :return: colores acertados
        """

        cont = 0

        for color in another_combination.colors:
            if color in self.colors:
                cont += 1

        return cont


class BrainBreaker:
    """
    Esta clase implementa unha partida do xogo, no que o usuario terá que adiviñar unha combinación de cores oculta que
    se creará no inicio nun máximo de 10 intentos.
    """
    MAX_INTENTOS: int = 10

    hidden_colors: ColorCombination
    intentos: list[ColorCombination]

    def __init__(self):
        """
        Constructor de clase
        """
        print("Benvido, comeza a partida")
        self.hidden_colors = ColorCombination()
        self.hidden_colors.generate_combination()
        self.intentos = []

    def show_game_phase(self) -> None:
        """
        Metodo que muestra por pantalla las instrucciones del juego, intentos realizados y aciertos
        """
        print("Combinacions utilizadas:")
        for intento in self.intentos:
            print("[",
                  intento.get_colors_as_string(),
                  "]",
                  "Colores en posicion incorrecta:",
                  intento.get_common_colors(self.hidden_colors)-intento.get_hits(self.hidden_colors),
                  "Colores en posicion correcta:",
                  intento.get_hits(self.hidden_colors))

        a = ColorCombination()
        a.colors = []
        for i in range(ColorCombination.COMBINATION_SIZE):
            """Pide los colores por pantalla"""
            color = int(input(f"Ingrese el color {i + 1} de la combinacion, 0=Rojo, 1=Verde, 2=Amarillo, 3=Rosa "))
            while color < 0 or color > 3:
                """En caso de introducir un numero erroneo lo vuelve a pedir"""
                color = int(input(f"Ingrese el color {i + 1} de la combinacion, 0=Rojo, 1=Verde, 2=Amarillo, 3=Rosa "))

            a.colors.append(color)


        """Muestra los aciertos"""
        print("Colores acertados en posición incorrecta:",
              a.get_common_colors(self.hidden_colors)-a.get_hits(self.hidden_colors))
        print("Colores acertados en posición correcta:", a.get_hits(self.hidden_colors))

        self.intentos.append(a)


    def is_game_over(self) -> bool:
        """
        Este metodo analiza si el juego ha terminado
        :return: si termina la partida
        """

        if self.intentos[-1].get_hits(self.hidden_colors) == ColorCombination.COMBINATION_SIZE:
            return True

        if len(self.intentos) >= self.MAX_INTENTOS:
            return True

        return False

    def show_final_message(self) -> None:
        """
        Este metodo muestra un mensaje al acabar la partida
        """
        if len(self.intentos) <= self.MAX_INTENTOS:
            print("Noraboa, gañou")
        else:
            print("Perdeu")


def main():
    """
    Metodo main que inicializa la aplicacion
    """
    resposta = "y"
    bb = BrainBreaker()
    while resposta == "y":
        bb.show_game_phase()
        if bb.is_game_over():
            bb.show_final_message()
            bb.intentos.clear()
            resposta = input("Queres xogar outra partida? y/n")

    print("Ata outra")


if __name__ == "__main__":
    main()