class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cnt = collections.OrderedDict()
        self.unique = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for key, value in self.cnt.items():
            return key
        return -1 

    def add(self, value: int) -> None:
        if value in self.unique:
            if value in self.cnt:
                del self.cnt[value]
        else:
            self.unique.add(value)
            self.cnt[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
