from bisect import bisect

from src.DictionaryVector import DictionaryVector
from src.VectorAbstract import VectorAbstract
from src.misc import StringToDict


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
        print(newVector)
        for i in range(self.size):
            newVector.SolveWith((self.keys[i], self.values[i]))
        index = newVector.ConvertToCanon()
        if index is None:
            return
        for e in self.values:
            e: VectorAbstract
            e.SolveWith((index, newVector))
        insertion = bisect(self.keys, index)
        self.keys.insert(insertion, index)
        self.values.insert(insertion, newVector)
        self.size+=1
        return


if __name__ == "__main__":
    I_RAW='''ABCAD 20
EBAAF 20
GHGXG 38
BEFBE 12
ABEFF 18
AEGBA 23
BBHEB 14
CAGFE 22
AAXBF 26
DFGEF 23'''
    INPUT=I_RAW.split("\n")
    M = list()
    for XRAW in INPUT:
        X=XRAW.split(" ")
        D=StringToDict(X[0])
        D["const"]=int(X[1])
        V = DictionaryVector(D)
        M.append(V)
    X = AutoSolvingMatrix(M)
    for i in range(X.size):
        print(X.keys[i],X.values[i])
    q = 1
'''ABC 8 (doesn't work for this one)
DEF 21
GHI 16
ADG 11
BEH 18
CFI 16
ABCDEFGHI 45'''