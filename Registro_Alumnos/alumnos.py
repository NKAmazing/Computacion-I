
class Student:
    
    def __init__(self, name="", lastname="", dni=int, email=""):
        self.__name = self.set_name(name)
        self.__lastname = self.set_lastname(lastname)
        self.__dni = self.set_dni(dni)
        self.__email = self.set_email(email)

    def __str__(self):
        return f"Name: {self.__name} Lastname: {self.__lastname} DNI: {self.__dni} Email: {self.__email}"

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

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni
        return dni

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
        return email

