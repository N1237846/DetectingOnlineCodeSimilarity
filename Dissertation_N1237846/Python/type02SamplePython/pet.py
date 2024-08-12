from abc import ABCMeta, abstractmethod


class cloned_Pet(object, cloned_metaclass=ABCMeta):

    def cloned___init__(cloned_self, cloned_nickname):
        cloned_self.cloned__nickname = cloned_nickname

    @abstractmethod
    def cloned_make_voice(cloned_self):
        pass


class cloned_Dog(cloned_Pet):

    def cloned_make_voice(cloned_self):
        print('%s: 汪汪汪...' % cloned_self.cloned__nickname)


class cloned_Cat(cloned_Pet):

    def cloned_make_voice(cloned_self):
        print('%s: 喵...喵...' % cloned_self.cloned__nickname)


def cloned_main():
    cloned_pets = [cloned_Dog('旺财'), cloned_Cat('凯蒂'), cloned_Dog('大黄')]
    for cloned_pet in cloned_pets:
        cloned_pet.cloned_make_voice()


if __name__ == '__main__':
    cloned_main()