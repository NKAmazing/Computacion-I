import main
import const
import time

def return_menu():
    print(const.JUMP_LINE)
    inp = input(const.QUESTION_RET)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(const.JUMP_LINE)
        time.sleep(0.5)
        print(const.RETURN_MENU)
        time.sleep(0.5)
    elif inp == 'n':
        exit_program()
        exit()
    else:
        error_menu()

def exit_program():
    print(const.JUMP_LINE)
    time.sleep(0.5)
    print(const.EXIT)
    time.sleep(0.5)

def error_menu():
    print(const.JUMP_LINE)
    print(const.ERR)
    time.sleep(0.5)
    print(const.JUMP_LINE)
    print(const.RETURN_MENU)
    time.sleep(0.5)