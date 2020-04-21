class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxst = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxst:
            self.maxst.append(x)
        else:
            self.maxst.append(max(self.maxst[-1], x))

    def pop(self) -> int:
        self.maxst.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxst[-1]

    def popMax(self) -> int:
        max_ = self.maxst.pop()
        tmp = []
        while self.stack[-1] != max_:
            tmp.append(self.pop())
        res = self.stack.pop()
        for i in range(len(tmp)-1, -1, -1):
            self.push(tmp[i])
        return res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
