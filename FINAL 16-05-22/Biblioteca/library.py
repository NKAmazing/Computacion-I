import time
from file import *
import const

class Library:

    def __init__(self):
        self.book_list = []
        self.book_dict = []
        self.client_list = []

    def add_to_list(self, book):
        print(const.JUMP_LINE)
        self.book_list.append(book)
        print(const.LOAD_DATA)

    def add_client_list(self, client):
        print(const.JUMP_LINE)
        self.client_list.append(client)
        print(const.CLIENT_ADDED)

    def add_to_file(self):
        print(const.JUMP_LINE)
        if len(self.book_list) != 0:
            file_operator(self.book_list)
            print(const.LOAD_DATA)
        else:
            print(const.EMPTY_Q)
        time.sleep(0.5)

    def show_list(self):
        print(const.JUMP_LINE)
        inp = input(const.QUESTION_SL)
        print(const.JUMP_LINE)
        if inp == 'bk':
            self.show_book_list()
        elif inp == 'cl':
            self.show_client_list()
        else:
            print(const.WRONG_LIST)
        time.sleep(0.5)

    def show_book_list(self):
        if len(self.book_list) != 0:
            for i in range(len(self.book_list)):
                print(self.book_list[i])
        else:
            print(const.EMPTY_LIST)

    def show_client_list(self):
        if len(self.client_list) != 0:
            for i in range(len(self.client_list)):
                print(self.client_list[i])
        else:
            print(const.EMPTY_CL)

    def delete_book(self):
        print(const.JUMP_LINE)
        self.show_list()
        inp = input(const.CHOOSE_BOOK)
        if inp >= (len(self.book_list) + 1):
            print(const.OUT_RANGE)
        else:
            self.book_list.pop(inp)
            print(const.BOOK_DEL)

    def delete_bk_list(self):
        print(const.JUMP_LINE)
        if len(self.book_list) != 0:
            file_rewrite(self.book_list)
            print(DEL_DATA)
        else:
            print(const.EMPTY_LR)
        time.sleep(0.5)

    def delete_cl(self):
        print(const.JUMP_LINE)
        if len(self.client_list) != 0:
            file_rewrite(self.client_list)
            print(DEL_DATA)
        else:
            print(const.EMPTY_LR2)
        time.sleep(0.5)

    def assign_client(self):
        print(const.JUMP_LINE)
        self.show_book_list()
        print(const.JUMP_LINE)
        inp = int(input(const.CHOOSE_BOOK))
        if inp >= (len(self.book_list) + 1):
            print(const.OUT_RANGE)
        else:
            print(const.JUMP_LINE)
            print(const.INP_FB, self.book_list[inp])
            print(const.JUMP_LINE)
            self.show_client_list()
            print(const.JUMP_LINE)
            inp_2 = int(input(const.CHOOSE_CLIENT))
            if inp_2 >= (len(self.client_list) + 1):
                print(const.OUT_RANGE)
            else:
                print(const.JUMP_LINE)
                print(const.INP_FB, self.client_list[inp_2])
                print(const.JUMP_LINE)
                self.book_dict[str(self.client_list[inp_2])] = (str(self.book_list[inp]))
                print(const.BK_ASSIGNED)
        time.sleep(0.5)

    def show_assigned(self):
        print(const.JUMP_LINE)
        if len(self.book_dict) != 0:
            for i in range(len(self.book_dict)):
                print(self.book_dict[i])
        else:
            print(const.EMPTY_DICT)
        time.sleep(0.5)

