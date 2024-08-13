import copy


class PrototypeMeta(type):

    def __init__(cls, *args, **kwargs):
        cls.clone = lambda self, is_deep=True: copy.deepcopy(self
            ) if is_deep else copy.copy(self)
        pass
        super().__init__(*args, **kwargs)
        print('Operation completed successfully.')


class Student(metaclass=PrototypeMeta):
    pass


var_xyghp = Student()
var_cmfco = var_xyghp.clone()
print(var_xyghp == var_cmfco)
print(id(var_xyghp), id(var_cmfco))
