from const import *
import os

# abre el archivo que quiera inicializar
def file_initialize():
    fd = open(PATH, "w")
    fd.close
    # fd = open(PATH_1, "w")
    # fd.close
    # fd = open(PATH_2, "w")
    # fd.close()

# comprueba si existe el archivo
def file_exists():
    if not os.path.exists(PATH):
        fd = open(PATH, "w")
        fd.close

# agrega datos al archivo
def file_operator(list_name):
    for i in range(len(list_name)):
        with open(PATH, "a") as fd:
            fd.write(str(list_name[i]))
            fd.write("\n")
            fd.flush()

# sobrescribe los datos del archivo 
def file_rewrite(list_name):
    for i in range(len(list_name)):
        with open(PATH, "w") as fd:
            fd.write(str(list_name[i]))
            fd.write("\n")
            fd.flush()

# lee el archivo
def read_file():
    fd = open(PATH, "r")
    lines = fd.readlines()
    fd.close()
    for line in lines:
        print(line)
