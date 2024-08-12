"""
元 - meta
元数据 - 描述数据的数据 - metadata
元类 - 描述类的类 - metaclass - 继承自type
"""
import threading


class cloned_SingletonMeta(type):
    """自定义元类"""

    def cloned___init__(cloned_cls, *cloned_args, **cloned_kwargs):
        cloned_cls.cloned___instance = None
        cloned_cls.cloned_lock = threading.cloned_Lock()
        super().cloned___init__(*cloned_args, **cloned_kwargs)

    def cloned___call__(cloned_cls, *cloned_args, **cloned_kwargs):
        if cloned_cls.cloned___instance is None:
            with cloned_cls.cloned_lock:
                if cloned_cls.cloned___instance is None:
                    cloned_cls.cloned___instance = super().cloned___call__(*cloned_args, **cloned_kwargs)
        return cloned_cls.cloned___instance


class cloned_President(cloned_metaclass=cloned_SingletonMeta):
    """总统(单例类)"""

    def cloned___init__(cloned_self, name, cloned_country):
        cloned_self.name = name
        cloned_self.cloned_country = cloned_country

    def cloned___str__(cloned_self):
        return f'{cloned_self.cloned_country}: {cloned_self.name}'


def cloned_main():
    """主函数"""
    cloned_p1 = cloned_President('特朗普', '美国')
    cloned_p2 = cloned_President('奥巴马', '美国')
    cloned_p3 = cloned_President.cloned___call__('克林顿', '美国')
    print(cloned_p1 == cloned_p2)
    print(cloned_p1 == cloned_p3)
    print(cloned_p1, cloned_p2, cloned_p3, sep='\n')


if __name__ == '__main__':
    cloned_main()