class Insert:
    def __init__(self, indA, l):
        self.indexA = indA
        self.letter = l


class Delete:
    def __init__(self, indA):
        self.indexA = indA


class Update:
    def __init__(self, indA, l):
        self.indexA = indA
        self.letter = l

class FakeUpdate:
    def __init__(self, indA, l):
        self.indexA = indA
        self.letter = l
