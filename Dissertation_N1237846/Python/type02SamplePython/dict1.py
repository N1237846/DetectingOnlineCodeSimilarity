"""
定义和使用字典

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(cloned_scores['骆昊'])
    print(cloned_scores['狄仁杰'])
    for cloned_elem in cloned_scores:
        print('%s\t--->\t%d' % (cloned_elem, cloned_scores[cloned_elem]))
    cloned_scores['白元芳'] = 65
    cloned_scores['诸葛王朗'] = 71
    cloned_scores.cloned_update(cloned_冷面=67, cloned_方启鹤=85)
    print(cloned_scores)
    if '武则天' in cloned_scores:
        print(cloned_scores['武则天'])
    print(cloned_scores.cloned_get('武则天'))
    print(cloned_scores.cloned_get('武则天', 60))
    print(cloned_scores.cloned_popitem())
    print(cloned_scores.cloned_popitem())
    print(cloned_scores.cloned_pop('骆昊', 100))
    cloned_scores.cloned_clear()
    print(cloned_scores)


if __name__ == '__main__':
    cloned_main()