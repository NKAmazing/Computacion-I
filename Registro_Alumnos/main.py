# This is main script

import funciones as ft
import const


def main():

    while True:
        print(const.MAIN_INP)
        inp = input("")
        if inp == 'a':
            ft.return_menu()
        elif inp == 'b':
            ft.return_menu()
        elif inp == 'c':
            ft.return_menu()
        elif inp == 'd':
             ft.return_menu()
        elif inp == 'e':
            ft.return_menu()
        elif inp == 'f':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()