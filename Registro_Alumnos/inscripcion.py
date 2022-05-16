from alumnos import Student
import const
from materias import *
from main import *


class Inscription:

    def __init__(self, student="", asignature="", dt_insc=""):
        self.__student = self.set_student(student)
        self.__asignature = self.set_asignature(asignature)
        self.__dt_insc = self.set_dt_insc(dt_insc)

    def get_student(self):
        return self.__student

    def set_student(self, student):
        self.__student = student
        return student

    def get_asignature(self):
        return self.__asignature

    def set_asignature(self, asignature):
        self.__asignature = asignature
        return asignature

    def get_dt_insc(self):
        return self.__dt_insc

    def set_dt_insc(self, dt_insc):
        self.__dt_insc = dt_insc
        return dt_insc

    def inscription(self, student, asignature):
        students = Student()
        students.dni_validation(student)
        if students.dni_validation(student) == False:
            print(const.INSC_FALSE)
            return
        asign = Asignature()
        asign.add_student(student, asignature)
        # asign.add_student(student, asign_2)
        # asign.add_student(student, asign_3)
        print(const.INSC_TRUE)
