import const
from clients import Client
import file
import time

class Bank:

    def __init__(self):
        self.queue_list = []
        self.queue_list_2 = []
        self.treated_list = []

    def clients_append(self, client):
        if len(self.queue_list) <= len(self.queue_list_2):
            if client.state == 0:
                self.queue_list.append(str(client))
                file.file_operator(self.queue_list)
                print(self.queue_list)
            else:
                print(const.ERR)
        else:
            if client.state == 0:
                self.queue_list_2.append(str(client))
                file.file_operator_2(self.queue_list_2)
                print(self.queue_list_2)
            else:
                print(const.ERR)

    def show_queue(self):
        print(const.JUMP_LINE)
        inp = int(input(const.INP))
        if inp == 1:
            print(const.JUMP_LINE)
            print(self.queue_list)
        elif inp == 2:
            print(const.JUMP_LINE)
            print(self.queue_list_2)
        else:
            print(const.ERR)
        return

    def show_cls_treated(self):
        # file.file_clients_treated()
        # return
        if len(self.treated_list) != 0:
            print(self.treated_list)
        else:
            print(const.EMPTY_T)

    def treat_client(self):
        inp = int(input(const.INP_Q))
        if inp == 1:
            if len(self.queue_list) != 0:
                for client in range(len(self.queue_list) - 1, -1, -1):
                    print(f"Treating with client {self.queue_list[client]}")
                    time.sleep(1)
                    self.treated_list.append(self.queue_list[client])
                    self.queue_list.pop(client)
                print(self.queue_list)
            else:
                print(const.EMPTY_Q)
        elif inp == 2:
            if len(self.queue_list_2) != 0:
                for client in range(len(self.queue_list_2) - 1, -1, -1):
                    print(f"Treating with client {self.queue_list_2[client]}")
                    time.sleep(1)
                    self.treated_list.append(self.queue_list_2[client])
                    self.queue_list_2.pop(client)    
                print(self.queue_list_2)
            else:
                print(const.EMPTY_Q)
        else:
            print(const.ERR)