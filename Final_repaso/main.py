# This is main script

from clients import Client
from bank import *
import const
import functions as ft

# objects settled
bank = Bank()

client1 = Client("Nicolas", "Mayoral", 42670639, 0)
client2 = Client("Juan", "Sueta", 42129530, 0)
client3 = Client("Francisco", "Rodeles", 43220870, 1)
client4 = Client("Julian", "Castillo", 42100123, 0)
client5 = Client("Alexis", "Lino", 42820135, 0)
client6 = Client("Aaron", "Moya", 42860245, 0)

bank.clients_append(client1)
bank.clients_append(client2)
bank.clients_append(client3)
bank.clients_append(client4)
bank.clients_append(client5)
bank.clients_append(client6)

def main():
    while True:
        print(const.MAIN_INP)
        inp = input(": ")
        if inp == 'a':
            bank.show_queue()
            ft.return_menu()
        elif inp == 'b':
            bank.show_cls_treated()
            ft.return_menu()
        elif inp == 'c':
            bank.treat_client()
            ft.return_menu()        
        elif inp == 'd':
                ft.exit_program()
                break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()