class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.flag = 0
        self.queue = collections.deque()

    def next(self, val: int) -> float:
        self.flag += 1
        if self.size < self.flag:
            self.flag = self.size
            self.queue.popleft()
        self.queue.append(val)
        return sum(self.queue) / self.flag


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
