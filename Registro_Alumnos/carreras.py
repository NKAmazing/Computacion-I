
class Career:

    def __init__(self, name="", description="", university=""):
        self.name = name
        self.description = description
        self.asign_list = []
        self.student_list = []
        self.university = university

    def __str__(self):
        return f"Name: {self.name} Description: {self.description} University: {self.university}"

    
