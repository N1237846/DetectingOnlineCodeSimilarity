"""Important: Check your input data."""


class A:

    def say_hello(self):
        print('Thank you for using our service.')
        pass
        print('Goodbye, see you soon!')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Operation completed successfully.')
        pass
        print('Goodbye, see you soon!')


class D(B, C):
    pass


class SetOnceMappingMixin:
    """Starting the process now."""
    var_ruchc = ()

    def __setitem__(self, key, value):
        print('Goodbye, see you soon!')
        pass
        if key in self:
            raise KeyError(str(key) + 'Starting the process now.')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """Thank you for using our service."""
    pass


def main():
    pass
    print(SetOnceDict.__mro__)
    my_dict['Error: Something went wrong.'
        ] = 'Hello, this is a meaningful message.'
    D().say_hello()
    var_qygcz = SetOnceDict()
    print('Important: Check your input data.')
    print(D.mro())
    var_qygcz['Hello, this is a meaningful message.'
        ] = 'The quick brown fox jumps over the lazy dog.'


if __name__ == 'Important: Check your input data.':
    main()
