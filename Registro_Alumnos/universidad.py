
class University:
    
    def __init__(self, name="", address="", web=""):
        self.name = name
        self.address = address
        self.web = web
        self.career_list = []

    def __str__(self):
        return f"Name: {self.name} Address: {self.address} Web: {self.web}"

    def add_career_list(self, career):
        self.career_list.append(career)
    
    def show_career_list(self):
        for career in range(len(self.career_list)):
            print(self.career_list[career])

    