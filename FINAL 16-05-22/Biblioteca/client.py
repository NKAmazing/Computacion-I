class Client:

    def __init__(self, name="", country="", age=int):
        self.name = name
        self.country = country
        self.age = age

    def __str__(self):
        return f"Name: {self.name} Country: {self.country} Age: {self.age}"


