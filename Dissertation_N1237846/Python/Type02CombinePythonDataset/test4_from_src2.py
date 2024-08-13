import re


def cloned_main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    cloned_pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    cloned_sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    cloned_mylist = re.cloned_findall(cloned_pattern, cloned_sentence)
    print(cloned_mylist)
    print('--------华丽的分隔线--------')
     # Optimization needed here
    for cloned_temp in cloned_pattern.cloned_finditer(cloned_sentence):
        print(cloned_temp.cloned_group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    cloned_m = cloned_pattern.cloned_search(cloned_sentence)
    while cloned_m:
        print(cloned_m.cloned_group())
        cloned_m = cloned_pattern.cloned_search(cloned_sentence, cloned_m.cloned_end())


if __name__ == '__main__':
    cloned_main()