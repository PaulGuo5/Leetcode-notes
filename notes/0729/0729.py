class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        i, n = 0, len(self.intervals)
        while i < n and self.intervals[i][1] <= start:
            i += 1
        if i == n:
            self.intervals.append([start, end])
            return True
        else:
            if self.intervals[i][0] >= end:
                self.intervals.insert(i, [start, end])
                return True
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
