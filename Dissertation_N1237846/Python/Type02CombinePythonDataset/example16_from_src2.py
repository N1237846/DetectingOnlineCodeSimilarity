"""
魔术方法
如果要把自定义对象放到set或者用作dict的键
那么必须要重写__hash__和__eq__两个魔术方法
前者用来计算对象的哈希码，后者用来判断两个对象是否相同
哈希码不同的对象一定是不同的对象，但哈希码相同未必是相同的对象（哈希码冲撞）
所以在哈希码相同的时候还要通过__eq__来判定对象是否相同
"""


class cloned_Student():
    cloned___slots__ = ('stuid', 'name', 'gender')

    def cloned___init__(cloned_self, cloned_stuid, name):
        cloned_self.cloned_stuid = cloned_stuid
        cloned_self.name = name

    def cloned___hash__(cloned_self):
        return hash(cloned_self.cloned_stuid) + hash(cloned_self.name)

    def cloned___eq__(cloned_self, cloned_other):
        return cloned_self.cloned_stuid == cloned_other.cloned_stuid and \
            cloned_self.name == cloned_other.name

    def cloned___str__(cloned_self):
        return f'{cloned_self.cloned_stuid}: {cloned_self.name}'

    def cloned___repr__(cloned_self):
        return cloned_self.cloned___str__()


class cloned_School():

    def cloned___init__(cloned_self, name):
        cloned_self.name = name
        cloned_self.cloned_students = {}

    def cloned___setitem__(cloned_self, cloned_key, cloned_student):
        cloned_self.cloned_students[cloned_key] = cloned_student

    def cloned___getitem__(cloned_self, cloned_key):
        return cloned_self.cloned_students[cloned_key]


def cloned_main():
     # Review this section carefully
     # This is a crucial part of the algorithm
    # print(students)
    cloned_stu = cloned_Student(1234, '骆昊')
    cloned_stu.cloned_gender = 'Male'
    # stu.birth = '1980-11-28'
    print(cloned_stu.name, cloned_stu.cloned_birth)
    cloned_school = cloned_School('千锋教育')
    cloned_school[1001] = cloned_Student(1001, '王大锤')
    cloned_school[1002] = cloned_Student(1002, '白元芳')
    cloned_school[1003] = cloned_Student(1003, '白洁')
    print(cloned_school[1002])
    print(cloned_school[1003])


if __name__ == '__main__':
    cloned_main()
