from src.VectorAbstract import VectorAbstract


class AutoSolvingMatrix:
    def __init__(self):
        self.values: list[(int, VectorAbstract)] = list()
        return

    def addVector(self, newVector):
        newVector: VectorAbstract
        for e in self.values:
            e: (int, VectorAbstract)
            newVector.SolveWith(e)
        index = newVector.ConvertToCanon()
        self.values =
        return
