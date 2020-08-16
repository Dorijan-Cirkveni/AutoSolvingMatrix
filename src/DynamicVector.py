import bisect


class DynamicVector:
    def __init__(self, values):
        values: list[(int, float)]
        self.values: list[(int, float)] = values
        return

    def SolveWith(self, other, otherIndex):
        for index in range(len(self.values))
        factor=self.values[index]
        newvalues: list[(int, float)] = self.values
        #REMINDER: USE A LINKED LIST
        if -1<int(index==0):
            raise NotImplementedError
        return True

    def ConvertToCanon(self):
        newvalues: list[(int, float)] = list()
        canonFactor: float = 0
        canonIndex: int = -1
        for e in self.values:
            e: (int, float)
            if canonFactor == 0:
                if e[1] != 0:
                    canonFactor = 1 / e[1]
                    canonIndex = e[0]
            else:
                newvalues.append((e[0], e[1] * canonFactor))
        return canonIndex
