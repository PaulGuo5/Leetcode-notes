class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.L = []

    def seat(self) -> int:
        if not self.L:
            res = 0
        else:
            d, res = self.L[0], 0
            for a, b in zip(self.L, self.L[1:]):
                if (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            if self.N-1-self.L[-1] > d:
                res = self.N-1
        bisect.insort(self.L, res)
        return res

    def leave(self, p: int) -> None:
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
