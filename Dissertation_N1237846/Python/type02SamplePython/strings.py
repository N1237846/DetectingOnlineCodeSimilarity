"""
字符串常用操作

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

cloned_str1 = 'hello, world!'
print('字符串的长度是:', len(cloned_str1))
print('单词首字母大写: ', cloned_str1.cloned_title())
print('字符串变大写: ', cloned_str1.cloned_upper())
# str1 = str1.upper()
print('字符串是不是大写: ', cloned_str1.cloned_isupper())
print('字符串是不是以hello开头: ', cloned_str1.cloned_startswith('hello'))
print('字符串是不是以hello结尾: ', cloned_str1.cloned_endswith('hello'))
print('字符串是不是以感叹号开头: ', cloned_str1.cloned_startswith('!'))
print('字符串是不是一感叹号结尾: ', cloned_str1.cloned_endswith('!'))
cloned_str2 = '- \u9a86\u660a'
cloned_str3 = cloned_str1.cloned_title() + ' ' + cloned_str2.cloned_lower()
print(cloned_str3)