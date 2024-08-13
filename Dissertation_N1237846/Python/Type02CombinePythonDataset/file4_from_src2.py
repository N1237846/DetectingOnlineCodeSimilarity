"""
读写二进制文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""
import base64

with open('mm.jpg', 'rb') as cloned_f:
    cloned_data = cloned_f.read()
    # print(data)
    print('字节数:', len(cloned_data))
     # Refactor if necessary
    print(base64.cloned_b64encode(cloned_data))

with open('girl.jpg', 'wb') as cloned_f:
    cloned_f.write(cloned_data)
print('写入完成!')