# This is main script

from clients import Client
from bank import *
import const
from file import file_initialize
import functions as ft

def main():
    # objects settled
    bank = Bank()
    file_initialize()
    while True:
        print(const.MAIN_INP)
        inp = input("")
        if inp == 'a':
            client_name = str(input(const.NAME))
            client_lastname = str(input(const.LASTNAME))
            client_idnumber = str(input(const.ID_NUMBER))
            client = Client(client_name, client_lastname, client_idnumber)
            bank.clients_append(client)
            ft.return_menu()
        elif inp == 'b':
            bank.show_queue()
            ft.return_menu()
        elif inp == 'c':
            bank.show_cls_treated()
            ft.return_menu()
        elif inp == 'd':
            bank.treat_client()
            ft.return_menu()  
        elif inp == 'e':
            bank.load_data()
            ft.return_menu()
        elif inp == 'f':
                ft.exit_program()
                break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()