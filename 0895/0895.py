class FreqStack:

    def __init__(self):
        self.cnt = collections.Counter()
        self.freq = collections.defaultdict(list)
        self.max_cnt = 0 

    def push(self, x: int) -> None:
        self.cnt[x] += 1
        cnt_x = self.cnt[x]
        if cnt_x > self.max_cnt:
            self.max_cnt = cnt_x
        self.freq[cnt_x].append(x)
        

    def pop(self) -> int:
        tmp = self.freq[self.max_cnt].pop()
        self.cnt[tmp] -= 1
        if not self.freq[self.max_cnt]:
            self.max_cnt -= 1
        return tmp

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
