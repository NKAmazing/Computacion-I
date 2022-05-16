import const


class Asignature:

    def __init__(self, name="", code=int):
        self.name = name
        self.__code = self.set_code(code)
        self.students_dict = {}

    def __str__(self):
        return f"Name: {self.name} Code: {self.__code}"

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code
        return code

    def add_student(self, student, list_of_asign):
        if str(student.name) not in self.students_dict:
            self.students_dict[str(student.name)] = list()
        student = str(student.name)
        self.students_dict[student].extend(list_of_asign)
        return self.students_dict

    def show_students(self):
        inp = input(const.INP_A)
        for student in range(len(self.students_dict)):
            print(self.students_dict[student])
