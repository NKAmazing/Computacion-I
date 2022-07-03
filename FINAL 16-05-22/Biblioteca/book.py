class Book:

    def __init__(self, name="", author="", ISB=""):
        self.name = name
        self.author = author
        self.ISB = ISB

    def __str__(self):
        return f"Name: {self.name} Author: {self.author} ISB: {self.ISB}"
