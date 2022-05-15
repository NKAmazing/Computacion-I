
class Inscription:

    def __init__(self, student="", assignature="", dt_insc=""):
        self.__student = self.set_student(student)
        self.__assignature = self.set_assignature(assignature)
        self.__dt_insc = self.set_dt_insc(dt_insc)

    def get_student(self):
        return self.__student

    def set_student(self, student):
        self.__student = student
        return student

    def get_assignature(self):
        return self.__assignature

    def set_assignature(self, assignature):
        self.__assignature = assignature
        return assignature

    def get_dt_insc(self):
        return self.__dt_insc

    def set_dt_insc(self, dt_insc):
        self.__dt_insc = dt_insc
        return dt_insc
