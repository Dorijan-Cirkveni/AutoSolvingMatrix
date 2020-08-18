from bisect import bisect

from src.DictionaryVector import DictionaryVector
from src.VectorAbstract import VectorAbstract


class AutoSolvingMatrix:
    def __init__(self, vectors=None):
        if vectors is None:
            vectors = list()
        self.keys: list[int] = list()
        self.values: list[VectorAbstract] = list()
        self.size = 0
        for e in vectors:
            self.addVector(e)
        return

    def addVector(self, newVector):
        newVector: VectorAbstract
        for i in range(self.size):
            newVector.SolveWith((self.keys[i], self.values[i]))
        index = newVector.ConvertToCanon()
        for e in self.values:
            e:VectorAbstract
            e.SolveWith((index,newVector))
        insertion = bisect(self.keys, index)
        self.keys.insert(insertion, index)
        self.values.insert(insertion, newVector)
        return


if __name__ == "__main__":
    A = DictionaryVector({1: 1, 2: -1})
    B = DictionaryVector({2: 1, 3: -1})
    X = AutoSolvingMatrix([A,B])
    q = 1
