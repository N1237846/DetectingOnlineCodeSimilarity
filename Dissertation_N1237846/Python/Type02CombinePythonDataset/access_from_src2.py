class cloned_Test:

    def cloned___init__(cloned_self, cloned_foo):
        cloned_self.cloned___foo = cloned_foo

    def cloned___bar(cloned_self):
        print(cloned_self.cloned___foo)
        print('__bar')


def cloned_main():
    test = cloned_Test('hello')
    test.cloned__Test__bar()
    print(test.cloned__Test__foo)


if __name__ == "__main__":
    cloned_main()