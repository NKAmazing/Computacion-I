class Client:

    def __init__(self, name="", lastname="", id_number=int, state=0):
        self.__name = self.set_name(name)
        self.__lastname = self.set_lastname(lastname)
        self.__id_number = self.set_id_number(id_number)
        self.clients = []
        self.state = state # state 0 no atendido

    def __str__(self):
        return f"Name: {self.__name} Lastname: {self.__lastname} ID Number: {self.__id_number} State: {self.state}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return name

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname
        return lastname

    def get_id_number(self):
        return self.__id_number
    
    def set_id_number(self, id_number):
        self.__id_number = id_number
        return id_number


