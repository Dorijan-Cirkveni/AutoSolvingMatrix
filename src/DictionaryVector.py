from src.VectorAbstract import VectorAbstract


class DictionaryVector(VectorAbstract):
    def __init__(self, values=None):
        if values is None:
            values = dict()
        self.values: dict = dict()
        for e in values:
            v = values[e]
            if v != 0:
                self.values[e] = v
        return

    def FindSolvables(self, potentials):
        potentials: set
        return potentials.intersection(set(self.values.keys()))

    def SolveWith(self, other):
        other: (int, DictionaryVector)
        if other[0] not in self.values:
            return
        factor = self.values.pop(other[0])
        otv: DictionaryVector = other[1]
        for e in otv.values:
            if e not in self.values:
                self.values[e] = 0
            newvalue = self.values[e] - otv.values[e] * factor
            if newvalue == 0:
                self.values.pop(e)
            else:
                self.values[e] = newvalue
        return

    def ConvertToCanon(self):
        minvalue = min(self.values.keys())
        factor = self.values.pop(minvalue)
        for e in self.values:
            self.values[e] /= factor
        return minvalue


if __name__ == "__main__":
    A = DictionaryVector({3: 2})
    B = DictionaryVector({1:2, 2: 2, 3: 2})
    B.SolveWith((1,A))
    print("Done!")
