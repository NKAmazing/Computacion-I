import const
import functions as ft
from library import *
from book import *
from client import *

book1 = Book("A storm of Swords", "George RR Martin", "1234")
book2 = Book("Clash of Kings", "George RR Martin", "5678")
book3 = Book("A Dance of Dragons", "George RR Martin", "1243")


def main():
    library = Library()
    ft.set_objects()
    while True:
        print(const.MENU)
        inp = input("")
        inp = inp.lower()
        if inp == 'a':
            book_name = input(const.NAME)
            book_author = input(const.AUTHOR)
            book_ISB = input(const.ISB)
            book = Book(book_name, book_author, book_ISB)
            library.add_to_list(book)
            ft.return_menu()
        elif inp == 'b':
            library.show_list()
            ft.return_menu()
        elif inp == 'c':
            client_name = input(const.NAME)
            client_country = input(const.COUNTRY)
            client_age = input(const.AGE)
            client = Client(client_name, client_country, client_age)
            library.add_client_list(client)
            ft.return_menu()
        elif inp == 'd':
            library.assign_client()
            ft.return_menu()
        elif inp == 'e':
            library.show_assigned()
            ft.return_menu()
        elif inp == 'f':
            library.add_to_file()
            ft.return_menu()
        elif inp == 'g':
            library.delete_book()
            ft.return_menu()
        elif inp == 'h':
            ft.help_function()
            ft.return_menu()
        elif inp == 'i':
            library.delete_bk_list()
            ft.return_menu()
        elif inp == 'q':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()