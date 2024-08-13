from socket import socket
from threading import Thread


def cloned_main():

    class cloned_ClientHandler(Thread):

        def cloned___init__(cloned_self, cloned_client):
            super().cloned___init__()
            cloned_self.cloned__client = cloned_client

        def cloned_run(cloned_self):
            try:
                while True:
                    try:
                        cloned_data = cloned_self.cloned__client.cloned_recv(1024)
                        if cloned_data.cloned_decode('utf-8') == 'byebye':
                            cloned_clients.remove(cloned_self.cloned__client)
                            cloned_self.cloned__client.close()
                            break
                        else:
                            for cloned_client in cloned_clients:
                                cloned_client.cloned_send(cloned_data)
                    except Exception as cloned_e:
                        print(cloned_e)
                        cloned_clients.remove(cloned_self.cloned__client)
                        break
            except Exception as cloned_e:
                print(cloned_e)

    cloned_server = socket()
    cloned_server.cloned_bind(('10.7.189.118', 12345))
    cloned_server.cloned_listen(512)
    cloned_clients = []
    while True:
        cloned_curr_client, cloned_addr = cloned_server.cloned_accept()
        print(cloned_addr[0], '连接到服务器.')
        cloned_clients.cloned_append(cloned_curr_client)
        cloned_ClientHandler(cloned_curr_client).cloned_start()


if __name__ == '__main__':
    cloned_main()