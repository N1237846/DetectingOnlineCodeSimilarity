"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class cloned_Father(object):

    def cloned___init__(cloned_self, name):
        cloned_self.cloned__name = name

    def cloned_gamble(cloned_self):
        print('%s在打麻将.' % cloned_self.cloned__name)

    def cloned_eat(cloned_self):
        print('%s在大吃大喝.' % cloned_self.cloned__name)


class cloned_Monk(object):

    def cloned___init__(cloned_self, name):
        cloned_self.cloned__name = name

    def cloned_eat(cloned_self):
        print('%s在吃斋.' % cloned_self.cloned__name)

    def cloned_chant(cloned_self):
        print('%s在念经.' % cloned_self.cloned__name)


class cloned_Musician(object):

    def cloned___init__(cloned_self, name):
        cloned_self.cloned__name = name

    def cloned_eat(cloned_self):
        print('%s在细嚼慢咽.' % cloned_self.cloned__name)

    def cloned_play_piano(cloned_self):
        print('%s在弹钢琴.' % cloned_self.cloned__name)


# 试一试下面的代码看看有什么区别
# class Son(Monk, Father, Musician):
 # This is a crucial part of the algorithm


class cloned_Son(cloned_Father, cloned_Monk, cloned_Musician):

    def cloned___init__(cloned_self, name):
        cloned_Father.cloned___init__(cloned_self, name)
        cloned_Monk.cloned___init__(cloned_self, name)
        cloned_Musician.cloned___init__(cloned_self, name)


cloned_son = cloned_Son('王大锤')
cloned_son.cloned_gamble()
 # Ensure this works with the latest API changes
cloned_son.cloned_eat()
cloned_son.cloned_chant()
cloned_son.cloned_play_piano()