# This is main script

import funciones as ft
import const
from alumnos import *
from inscripcion import *
from materias import *
from objects import *
from universidad import *
from carreras import *

university = University()
# asign = Asignature()
insc = Inscription()

asign_1 = Asignature("Computacion", 12345)
asign_2 = Asignature("Programacion", 67890)
asign_3 = Asignature("Estadistica", 12436)

engineering = Career("Software Engineering", "Eng of software and informatic devices", "UM")
architecture = Career("Architecture", "Archi career", "UM")

engineering.add_asign(asign_1)

student_1 = Student("Nicolas", "Mayoral", 42670639, "n.mayoral@alumno.um.edu.ar")

university.add_career_list(engineering)
university.add_career_list(architecture)

# asign.add_student(student_1, asign_1)
# asign.add_student(student_1, asign_2)
# asign.add_student(student_1, asign_3)

def main():
    while True:
        print(const.MAIN_INP)
        inp = input("")
        if inp == 'a':
            insc.inscription(student_1, asign_1)
            ft.return_menu()
        elif inp == 'b':
            ft.return_menu()
        elif inp == 'c':
            asign_1.show_students()
            ft.return_menu()
        elif inp == 'd':
             ft.return_menu()
        elif inp == 'e':
            university.show_career_list()
            ft.return_menu()
        elif inp == 'f':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()