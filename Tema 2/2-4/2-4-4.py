class Wallet:
    """
    Classe de wallet que dependiendo del dinero y de una tarjeta te manda a sacar dinero
    """
    money:float
    card:bool

    def __init__(self, money:float, card:bool):
        self.money = money
        self.card = card

    def available(self)->str:
        """
        Devuelve la accion a realizar
        :return: accion
        """
        if self.card:
            if self.money < 100 :
                return  "Vete ao caxeiro"
            else:
                return "Ten efectivo"
        else:
            if self.money < 100:
                return "Vai á sucursal"
            else:
                return "Ten efectivo"
def main():
    """
    Metodo main
    :return: accion de las tres carteras
    """
    wa = Wallet(250, False)
    wb = Wallet(25, True)
    wc = Wallet(10, False)

    print(wa.available())
    print(wb.available())
    print(wc.available())

if __name__ == '__main__':
    main()