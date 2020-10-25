class LogSystem:

    def __init__(self):
        self.times = []
        self.hashmap = {"Year":4, "Month":7, "Day":10, "Hour":13, "Minute":16, "Second":19}

    def put(self, id: int, timestamp: str) -> None:
        self.times.append([id, timestamp])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.hashmap[granularity]
        s, e = start[:idx], end[:idx]
        return [i for i, time in self.times if s <= time[:idx] <= e]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
