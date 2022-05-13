import os
from const import *


def file_operator(queue):
    if not os.path.exists(PATH):
        fd = open(PATH, "w")
        fd.close
    for i in range(len(queue)):
        with open(PATH, "a") as fd:
            fd.write(str(queue[i]))
            fd.write("\n")
            fd.flush()

def file_operator_2(queue):
    if not os.path.exists(PATH_1):
        fd = open(PATH_1, "w")
        fd.close
    for i in range(len(queue)):
        with open(PATH_1, "a") as fd:
            fd.write(str(queue[i]))
            fd.write("\n")
            fd.flush()

def file_treated(treated):
    if not os.path.exists(PATH_2):
        fd = open(PATH_2, "w")
        fd.close
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

