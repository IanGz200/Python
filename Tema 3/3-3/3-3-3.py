class Client:
    """
    Clase que simula un cliente
    """
    nif:str
    name:str
    surname:str

    def __init__(self, nif:str, name:str, surname:str):
        """
        Constructor de la clase Client
        :param nif: El nif del cliente
        :param name: El nombre del cliente
        :param surname: El apellido del cliente
        """
        self.nif = nif
        self.name = name
        self.surname = surname

class DataBase:
    """
    Clase que simula una base de datos de clientes
    """
    array_clientes:list[Client] = []

    def add_client(self)->None:
        """
        Agrega el cliente a la lista de clientes pidiendo sus datos por pantalla
        """
        nif:str = input("Introduzca el nif: ")
        name:str = input("Introduzca el nombre del cliente: ")
        surname:str = input("Introduzca el apellido del cliente: ")

        cl = Client(nif, name, surname)

        self.array_clientes.append(cl)

    def show_clients(self)->None:
        """
        Muestra el nif de todos los clientes
        :return: el nif por pantalla
        """
        for client in self.array_clientes:
            print(client.nif)

    def remove_client(self, nif:str)->None:
        """
        Borra de la lista el cliente con el nif que se pase por pantalla
        :param nif: El nif del cliente que se desea borrar
        """
        for client in self.array_clientes:
            if client.nif == nif:
                self.array_clientes.remove(client)

    def num_clients(self)->int:
        """
        Devuelve el numero de clientes en la lista que los guarda
        :return: numero de clientes
        """
        return len(self.array_clientes)

def main():
    db = DataBase()
    """Se crean dos clientes, se muestran sus nifs, se borra uno y se muestra el numero de clientes"""
    db.add_client()
    db.add_client()
    db.show_clients()
    db.remove_client(input("Introduzca el nif: "))
    print(db.num_clients())

if __name__ == "__main__":
    main()