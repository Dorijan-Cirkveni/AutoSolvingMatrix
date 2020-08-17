from llist import dllist, dllistnode

from src.VectorAbstract import VectorAbstract


class LinkedListVector(VectorAbstract):
    def __init__(self, content: list[(int, float)]):
        self.content: dllist = dllist()
        for e in content:
            self.content.appendright(e)
        return

    def SolveWith(self, other):
        other: (int, VectorAbstract)
        X = self.content.first
        for X in self.content:
            X: dllistnode
            if X.value >= other[0]:
                break
        if X.value != other[0]:
            return
        nx = X.prev
        f = self.content.pop(X)

    def ConvertToCanon(self):
        raise NotImplementedError
