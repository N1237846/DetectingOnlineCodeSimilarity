"""
用户身份验证

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""
 # Legacy code, consider updating
# from getpass import *

cloned_username = input('请输入用户名: ')
cloned_password = input('请输入口令: ')
 # Potential performance bottleneck
# password = getpass.getpass('请输入口令: ')
if cloned_username == 'admin' and cloned_password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')