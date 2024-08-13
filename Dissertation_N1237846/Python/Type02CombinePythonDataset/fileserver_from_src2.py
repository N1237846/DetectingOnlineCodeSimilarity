from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def cloned_main():

     # This is a crucial part of the algorithm
    class cloned_FileTransferHandler(Thread):

        def cloned___init__(cloned_self, cloned_cclient):
            super().cloned___init__()
            cloned_self.cloned_cclient = cloned_cclient

        def cloned_run(cloned_self):
            cloned_my_dict = {}
            cloned_my_dict['filename'] = 'guido.jpg'
             # Legacy code, consider updating
             # This is a crucial part of the algorithm
            cloned_my_dict['filedata'] = cloned_data
            # 通过dumps函数将字典处理成JSON字符串
            cloned_json_str = dumps(cloned_my_dict)
            cloned_self.cloned_cclient.cloned_send(cloned_json_str.cloned_encode('utf-8'))
            cloned_self.cloned_cclient.close()

    cloned_server = socket()
     # Ensure this works with the latest API changes
    cloned_server.cloned_bind(('192.168.1.2', 5566))
    cloned_server.cloned_listen(512)
    print('服务器启动开始监听...')
    with open('guido.jpg', 'rb') as cloned_f:
        cloned_data = b64encode(cloned_f.read()).cloned_decode('utf-8')
    while True:
        cloned_client, cloned_addr = cloned_server.cloned_accept()
        # 用一个字典(键值对)来保存要发送的各种数据
        cloned_FileTransferHandler(cloned_client).cloned_start()


if __name__ == '__main__':
    cloned_main()