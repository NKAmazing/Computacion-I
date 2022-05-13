import const
from clients import Client
import file

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
            elif client.state == 1:
                if client in self.queue_list:
                    self.queue_list.remove(client)
                    file.file_operator(self.queue_list)
                self.treated_list.append(str(client))
                file.file_treated(self.treated_list)
            else:
                print(const.ERR)
        else:
            if client.state == 0:
                self.queue_list_2.append(str(client))
                file.file_operator_2(self.queue_list_2)
                print(self.queue_list_2)
            elif client.state == 1:
                if client in self.queue_list_2:
                    self.queue_list_2.remove(client)
                    file.file_operator_2(self.queue_list_2)
                self.treated_list.append(str(client))
                file.file_treated(self.treated_list)
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
        file.file_clients_treated()
        return

    def treat_client(self):
        client = 0
        if len(self.queue_list) >= len(self.queue_list_2):
            for client in range(len(self.queue_list)):
                print(f"Treating with client {self.queue_list[client]}")
                # self.queue_list.pop(client)
        else:
            for client in range(len(self.queue_list_2)):
                print(f"Treating with client {self.queue_list_2[client]}")
                # self.queue_list.pop(client)