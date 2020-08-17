class VectorAbstract:
    def FindSolvables(self, potentials):
        raise NotImplementedError

    def SolveWith(self, other):
        other: (int,VectorAbstract)
        raise NotImplementedError

    def ConvertToCanon(self):
        raise NotImplementedError
