from builtins import round, float, len


class Entry:
    def __init__(self, char, listChar: list):
        self.R = char
        self.listChar = listChar

    def getCost(self, otherList: list):
        identical = 0
        for x in self.listChar:
            for y in otherList:
                if x == y:
                    identical += 1

        total = float(len(self.listChar) * len(otherList))
        return round(1.0 - (float(identical) / total), 3)


catalog = {}
catalog['R'] = Entry('R', ['G', 'A'])
catalog['M'] = Entry('M', ['A', 'C'])
catalog['S'] = Entry('S', ['G', 'C'])
catalog['V'] = Entry('V', ['G', 'A', 'C'])
catalog['N'] = Entry('N', ['G', 'U', 'A', 'C'])
catalog['G'] = Entry('G', ['G'])
catalog['U'] = Entry('U', ['U'])
catalog['A'] = Entry('A', ['A'])
catalog['C'] = Entry('C', ['C'])
