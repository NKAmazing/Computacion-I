
class Asignature:

    def __init__(self, name="", code=int):
        self.name = name
        self.__code = self.set_code(code)

    def __str__(self):
        return f"Name: {self.name} Code: {self.__code}"

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code
        return code
