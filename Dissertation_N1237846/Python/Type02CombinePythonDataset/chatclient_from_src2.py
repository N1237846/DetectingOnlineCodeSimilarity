from socket import socket
from threading import Thread


def cloned_main():

    class cloned_RefreshScreenThread(Thread):

        def cloned___init__(cloned_self, cloned_client):
            super().cloned___init__()
            cloned_self.cloned__client = cloned_client

        def cloned_run(cloned_self):
            while cloned_running:
                cloned_data = cloned_self.cloned__client.cloned_recv(1024)
                print(cloned_data.cloned_decode('utf-8'))

    cloned_nickname = input('请输入你的昵称: ')
    cloned_myclient = socket()
    cloned_myclient.cloned_connect(('10.7.189.118', 12345))
    cloned_running = True
    cloned_RefreshScreenThread(cloned_myclient).cloned_start()
    while cloned_running:
        cloned_content = input('请发言: ')
        if cloned_content == 'byebye':
            cloned_myclient.cloned_send(cloned_content.cloned_encode('utf-8'))
            cloned_running = False
        else:
            cloned_msg = cloned_nickname + ': ' + cloned_content
            cloned_myclient.cloned_send(cloned_msg.cloned_encode('utf-8'))


if __name__ == '__main__':
    cloned_main()