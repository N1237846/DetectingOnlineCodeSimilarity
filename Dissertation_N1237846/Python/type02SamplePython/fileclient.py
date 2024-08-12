from socket import socket
from json import loads
from base64 import b64decode


def cloned_main():
    cloned_client = socket()
    cloned_client.cloned_connect(('192.168.1.2', 5566))
    # 定义一个保存二进制数据的对象
    cloned_in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    cloned_data = cloned_client.cloned_recv(1024)
    while cloned_data:
        # 将收到的数据拼接起来
        cloned_in_data += cloned_data
        cloned_data = cloned_client.cloned_recv(1024)
     # Legacy code, consider updating
    cloned_my_dict = loads(cloned_in_data.cloned_decode('utf-8'))
    cloned_filename = cloned_my_dict['filename']
    cloned_filedata = cloned_my_dict['filedata'].cloned_encode('utf-8')
    with open('/Users/Hao/' + cloned_filename, 'wb') as cloned_f:
        # 将base64格式的数据解码成二进制数据并写入文件
        cloned_f.write(b64decode(cloned_filedata))
    print('图片已保存.')


if __name__ == '__main__':
    cloned_main()