# Constants

# paths
PATH = "E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\libros.txt"
PATH_1 = "E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\ejemplo_2.txt"
# paths con raw incluido (un solo backslash '\' )
PATH_2 = r"E:\Proyectos python\Computacion 1 FINAL\FINAL 16-05-22\N_Ejercicio\archives\ejemplo.txt"
PATH_3 = r"E:\Proyectos python\Computacion 1 FINAL\FINAL 16-05-22\N_Ejercicio\archives\ejemplo_2.txt"
# paths con format incluido
file_name = "ejemplo"
file_name_2 = "ejemplo_2"
PATH_4 = f"E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\archives\\{file_name}.txt"
PATH_5 = f"E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\archives\\{file_name_2}.txt"

# inputs
QUESTION_RET = "Do yo want to return to Main Menu? (Y/N) "
INP_A = "From what asignature do you want to check students? "
INP_Q = "What queue do you want to attend? 1/2 : "
INP_DB = "What queue do you want to add to database? 1/2 : "
NAME = "Enter name: "
LASTNAME = "Enter lastname: "
ID_NUMBER = "Enter ID Number: "
AUTHOR = "Enter Author: "
ISB = "Enter ISB: "
COUNTRY = "Enter country: "
AGE = "Enter Age: "
QUESTION_SL = "What list do you want to see? bk/cl : "

# errores o emptys
ERR = "UNEXPECTED ERROR"
EMPTY_Q = "This list is empty. No book to add to file."
EMPTY_Q_2 = "This queue is empty. No client to add to Database."
EMPTY_T = "This list of clients treated is empty."
EMPTY_LIST = "This list is empty. No book to add."
EMPTY_LR = "This list is empty. No book to delete."
EMPTY_LR2 = "This list is empty. No client to delete."
EMPTY_CL = "This list is empty. No client to add."
OUT_RANGE = "The object you selected is not in the list."
WRONG_LIST = "ERROR. The option you selected is not a list."
EMPTY_DICT = "This assigned book list is empty."

# menu
MENU = '''
MENU SOFTWARE NAME

OPTIONS:

    a) Option 1
    b) Option 2
    c) Option 3
    d) Option 4
    e) Option 5
    f) Option 6
    g) Option 7
    i) Option 8

    h) Help to use the software.

    q) Exit.

What do you want to do?

'''
# help
HELP = '''
HELP:

This is a help software for the user. 

Here you will find the instructions:

- instruction 1
- instruction 2
- instruction 3

'''


# mensajes
RETURN_MENU = "Returning to Main Menu..."
LOAD_DATA = "The data was successfully loaded."
CLIENT_ADDED = "The client was successfully added."
DEL_DATA = "The data has been deleted successfully from file."
CLIENT_ATTENDED = "All clients was successfully attended."
INSC_FALSE = "You cannot inscribed to this assignature."
INSC_TRUE = "You have successfully inscribed to the assignature."
NOT_INT_DNI = "Need to be a int digit!"
LEN_DNI = "Need to be a real Document!"
DNI_TRUE = "This DNI has validated successfully."
BOOK_DEL = "The book has been deleted from cataloge."
CHOOSE_BOOK = "Choose a Book from book list: "
CHOOSE_CLIENT = "Choose a Client from client list: "
BK_ASSIGNED = "The book was assigned to a client."
INP_FB = "You have chosen option: "

# operaciones de string
JUMP_LINE = "\n"

# mensajes de salida
EXIT = "Exiting the program..."