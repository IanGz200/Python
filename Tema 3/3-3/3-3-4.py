from typing import Dict


class Client:
    """
    Clase que simula un cliente
    """
    nif: str
    name: str
    surname: str

    def __init__(self, nif: str, name: str, surname: str):
        """
        Constructor de la clase Client
        :param nif: El nif del cliente
        :param name: El nombre del cliente
        :param surname: El apellido del cliente
        """
        self.nif = nif
        self.name = name
        self.surname = surname


class Contacts:
    """
    Clase que simula una lista telefónica de clientes
    """
    phonebook:Dict[int, Client] = {}

    def insert(self, tel:int , client:Client)->None:
        """
        Inserta un cliente en la lista
        :param tel: El telefono del cliente
        :param client: Cliente a insertar
        """
        self.phonebook[tel] = client

    def remove(self, tel:int)->None:
        """
        Elimina un cliente en la lista
        :param tel: El numero del cliente a eliminar
        """
        self.phonebook.pop(tel)

    def find_by_number(self, tel:int)->Client:
        """
        Encuentra un cliente en la lista
        :param tel: Telefono del cliente a encontrar
        :return: El cliente
        """
        return self.phonebook[tel]

    def num_contacts(self)->int:
        """
        Devuelve el numero de contactos
        :return: numero de contactos
        """
        return len(self.phonebook)

def main():
    contacts = Contacts()
    contacts.insert(697889999, Client(nif="0", name="Ian", surname="Gz"))
    contacts.insert(697889910, Client(nif="1", name="Dani", surname="Alvite"))
    contacts.insert(697888888, Client(nif="2", name="Jose", surname="Gonzalez"))
    print("Numero de contactos:",contacts.num_contacts())
    contacts.remove(697888888)
    print("Numero de contactos",contacts.num_contacts())
    print("El cliente con el numero 697889999 es:",contacts.find_by_number(697889999).name)

if __name__ == "__main__":
    main()