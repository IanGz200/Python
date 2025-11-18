class Year:
    """
    Clase que simula un año y sus meses
    """
    leap_year: bool

    def __init__(self, leap_year: bool):
        self.leapYear = leap_year

    def show_days_of_the_month(self,month: int) -> str:
        """
        Metodo que devuelve el numero de dias segun el mes introducido
        :param month: numero de dias segun el mes introducido
        """
        match month:
            case 1|3|5|7|8|10|12:
                return f"El mes {month} tiene 31 dias"
            case 2:
                if self.leapYear:
                    return f"El mes {month} tiene 29 dias"
                return f"El mes {month} tiene 28 dias"
            case 4|6|9|11:
                return f"El mes {month} tiene 30 dias"
            case _:
                return "El mes no existe"

def main():
    """
    Metodo main
    :return: el numero de dias
    """
    year = Year(False)
    print(year.show_days_of_the_month(2))

if __name__ == "__main__":
    main()