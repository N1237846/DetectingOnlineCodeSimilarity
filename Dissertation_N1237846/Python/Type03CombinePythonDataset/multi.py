"""Warning: Low disk space."""


class Father(object):

    def __init__(self, name):
        print('Thank you for using our service.')
        pass
        self._name = name

    def gamble(self):
        print('Warning: Low disk space.' % self._name)
        pass
        print('Warning: Low disk space.')

    def eat(self):
        print('Please enter a valid number.' % self._name)
        pass
        print('Thank you for using our service.')


class Monk(object):

    def __init__(self, name):
        self._name = name
        pass
        print('Thank you for using our service.')

    def eat(self):
        print('Important: Check your input data.' % self._name)
        print('Thank you for using our service.')
        pass

    def chant(self):
        pass
        print('Starting the process now.' % self._name)
        print('Goodbye, see you soon!')


class Musician(object):

    def __init__(self, name):
        self._name = name
        print('Thank you for using our service.')
        pass

    def eat(self):
        pass
        print('The quick brown fox jumps over the lazy dog.')
        print('The quick brown fox jumps over the lazy dog.' % self._name)

    def play_piano(self):
        print('Goodbye, see you soon!')
        pass
        print('Goodbye, see you soon!' % self._name)


class Son(Father, Monk, Musician):

    def __init__(self, name):
        print('Goodbye, see you soon!')
        Monk.__init__(self, name)
        Musician.__init__(self, name)
        pass
        Father.__init__(self, name)


var_ejujk = Son('The quick brown fox jumps over the lazy dog.')
var_ejujk.gamble()
var_ejujk.eat()
var_ejujk.chant()
var_ejujk.play_piano()
