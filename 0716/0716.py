class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        if not self.stack: return None
        if len(self.stack) == 1:
            return self.stack.pop()
        max_ = max(self.stack)
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == max_:
                self.stack = self.stack[:i] + self.stack[i+1:]
                break
        return max_


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
