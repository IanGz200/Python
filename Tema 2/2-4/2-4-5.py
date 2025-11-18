class StringComparator:
    """
    Clase que compara el largo de 3 strings
    """

    string1:str
    string2:str
    string3:str

    def __init__(self, string1:str, string2:str, string3:str):
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3

    def get_bigger(self):
        """
        Metodo que devuelve el string mas largo
        :return:
        """
        if len(self.string1) > len(self.string2):
            return self.string1
        else:
            if len(self.string2) > len(self.string3):
                return self.string2
            else:
                return self.string3
def main():
    """
    Metodo main
    :return: string mas largo
    """
    sc = StringComparator("hola", "adios", "largooooo")

    print(sc.get_bigger())

if __name__ == "__main__":
    main()