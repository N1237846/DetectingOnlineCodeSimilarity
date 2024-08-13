"""
不良内容过滤
"""
import re


def cloned_main():
    cloned_sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    cloned_purified = re.cloned_sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', cloned_sentence, cloned_flags=re.cloned_IGNORECASE)
    print(cloned_purified)


if __name__ == '__main__':
    cloned_main()