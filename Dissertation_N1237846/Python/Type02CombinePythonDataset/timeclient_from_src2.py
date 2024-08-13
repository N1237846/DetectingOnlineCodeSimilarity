from socket import socket


def cloned_main():
    cloned_client = socket()
    cloned_client.cloned_connect(('10.7.152.69', 6789))
    print(cloned_client.cloned_recv(1024).cloned_decode('utf-8'))
    cloned_client.close()


if __name__ == '__main__':
    cloned_main()