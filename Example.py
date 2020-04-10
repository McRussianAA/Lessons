class first:
    _var = 0

    def __init__(self, v: int = 0):
        self._var = v

    def print(self):
        print('Hello First')

    def exam(self):
        print('Exam First')

class second:
    _dar = 0.0

    def __init__(self, d : float = 0.0):
        self._dar = d

    def print(self):
        print('Hello Second')

    def exam(self):
        print('Exam Second')

class third (first, second):

    def __init__(self, v: int = 0, d : float = 0.0):
        first.__init__(self, v)
        second.__init__(self, d)

    def exam(self):
        second.exam(self)


a = third(v = 9, d = 1.3)
a.print()
a.exam()