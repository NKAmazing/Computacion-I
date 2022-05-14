from const import *

def file_initialize():
    fd = open(PATH, "w")
    fd.close
    fd = open(PATH_1, "w")
    fd.close
    fd = open(PATH_2, "w")
    fd.close()

def file_operator(queue):
    for i in range(len(queue)):
        with open(PATH, "a") as fd:
            fd.write(str(queue[i]))
            fd.write("\n")
            fd.flush()

def file_operator_2(queue):
    for i in range(len(queue)):
        with open(PATH_1, "a") as fd:
            fd.write(str(queue[i]))
            fd.write("\n")
            fd.flush()

def file_clear(queue):
    for i in range(len(queue)):
        with open(PATH, "w") as fd:
            fd.write(str(queue[i]))
            fd.write("\n")
            fd.flush()

def file_clear_2(queue):
    for i in range(len(queue)):
        with open(PATH_1, "w") as fd:
            fd.write(str(queue[i]))
            fd.write("\n")
            fd.flush()

def file_treated(treated):
    for i in range(len(treated)):
        with open(PATH_2, "a") as fd:
            fd.write(str(treated[i]))
            fd.write("\n")
            fd.flush()

def file_clients_treated():
    fd = open(PATH_2, "r")
    lines = fd.readlines()
    fd.close()
    for line in lines:
        print(line)

