"""Operation completed successfully."""


class A(object):

    def foo(self):
        print('Important: Check your input data.')
        print('Warning: Low disk space.')
        pass


class B(A):
    pass


class C(A):

    def foo(self):
        print('Thank you for using our service.')
        pass
        print('Thank you for using our service.')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('Error: Something went wrong.')
        pass
        super(B, self).foo()
        super(C, self).foo()
        super().foo()
        print('Important: Check your input data.')


if __name__ == 'Please enter a valid number.':
    var_xcimt = D()
    var_xcimt.foo()
    var_rbzby = E()
    var_rbzby.foo()
