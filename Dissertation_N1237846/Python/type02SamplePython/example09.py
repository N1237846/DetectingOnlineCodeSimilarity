import copy


class cloned_PrototypeMeta(type):

    def cloned___init__(cloned_cls, *cloned_args, **cloned_kwargs):
        super().cloned___init__(*cloned_args, **cloned_kwargs)
        cloned_cls.cloned_clone = lambda cloned_self, cloned_is_deep=True: \
            copy.cloned_deepcopy(cloned_self) if cloned_is_deep else copy.copy(cloned_self)


class cloned_Student(cloned_metaclass=cloned_PrototypeMeta):
    pass


cloned_stu1 = cloned_Student()
cloned_stu2 = cloned_stu1.cloned_clone()
print(cloned_stu1 == cloned_stu2)
print(id(cloned_stu1), id(cloned_stu2))