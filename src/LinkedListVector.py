from llist import dllist, dllistnode

from src.VectorAbstract import VectorAbstract


class LinkedListVector(VectorAbstract):
    def __init__(self,content:list[(int,float)]):
        self.content:dllist = dllist()
        for e in content:
            self.content.appendright(e)
        return

    def SolveWith(self, other):
        other: (int,VectorAbstract)
        for X in self.content:
            X:dllistnode
            if X.value>=self.content

    def ConvertToCanon(self):
        raise NotImplementedError
