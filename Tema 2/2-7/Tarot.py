class Tarot:
    """
    Programa que partindo das variables day, month e year como enteiros saque por pantalla o número de tarot. O programa
    verificará se a data é correcta (tendo en conta que o ano pode ser bisesto), senón sacará unha mensaxe de erro por
    pantalla.
    """
    day:int
    month:int
    year:int

    def __init__(self, day:int, month:int, year:int):
        """
        Constructor da clase Tarot
        :param day: dia del mes
        :param month: mes del año
        :param year: año
        """
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self, year:int) -> bool:
        """
        Metodo que comprueba que un año es bisiesto
        :param year: año a comprobar
        :return: Si es o no bisiesto
        """
        if (year%4==0 and year%100!=0) or year%400==0:
            return True
        else:
            return False

    def check_date(self, day:int, month:int, year:int)->bool:
        """
        Metodo que comprueba la validez de la fecha
        :param day: dia del mes, entre 0 y 32
        :param month: mes de año, entre 0 y 13
        :param year: año para comprobar si es bisiesto con otro metodo
        :return: Si la fecha introducida es válida
        """
        if 13 > month > 0:
            match month:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    if not 32 > day > 0:
                        return False
                case 2:
                    if self.is_leap_year(year):
                        if not 30 > day > 0:
                            return False
                    else:
                        if not 29 > day > 0:
                            return False
                case 4 | 6 | 9 | 11 | 12 | 15:
                    if not 31 > day > 0:
                        return False

            return True

        else:
            return False

    def calculate_tarot(self, day:int, month:int, year:int)->int:
        """
        Metodo que suma dias, mes y año para obtener el numero de tarot
        :param day: dia del mes
        :param month: mes del año
        :param year: año
        :return: numero del tarot, el cual está compuesto de la suma de todos los dígitos de suma
        """
        suma:int = day + month + year
        tarot_num:int = 0
        while len(str(suma))>1:

            for i in range(0,len(str(suma))):
                digito:int = suma%10
                suma = suma//10
                tarot_num += digito

        return tarot_num

def main():
    """
    Metodo main que crea un objeto Tarot y la pasa valores pidiendolos por pantalla
    :return: Devuelve por pantalla el numero de tarot
    """
    day:int = int(input("Introduzca el dia:"))
    month:int = int(input("Introduzca el mes:"))
    year:int = int(input("Introduzca el año:"))

    tarot = Tarot(day, month, year)
    """
    Comprueba que la fecha introducida es correcta
    """
    while not tarot.check_date(day, month, year):
        print("Introduzca una fecha valida:")
        day: int = int(input("Introduzca el dia:"))
        month: int = int(input("Introduzca el mes:"))
        year: int = int(input("Introduzca el año:"))

    print(tarot.calculate_tarot(day, month, year))

if __name__ == "__main__":
    main()