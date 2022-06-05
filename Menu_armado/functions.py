import const
import time
from main import *

def help_function():
    print(const.JUMP_LINE)
    time.sleep(0.5)
    print(const.HELP)
    time.sleep(0.5)

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

# def set_objects():
#     library = Library()
#     book1 = Book("A storm of Swords", "George RR Martin", "1234")
#     book2 = Book("Clash of Kings", "George RR Martin", "5678")
#     book3 = Book("A Dance of Dragons", "George RR Martin", "1243")
#     library.add_to_list(book1)
#     library.add_to_list(book2)
#     library.add_to_list(book3)
#     client1 = Client("Nicolas", "Argentina", 22)
#     client2 = Client("Juan", "Argentina", 22)
#     client3 = Client("Francisco", "Argentina", 21)
#     library.add_client_list(client1)
#     library.add_client_list(client2)
#     library.add_client_list(client3)

