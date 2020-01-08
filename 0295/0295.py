class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        return self.nums[len(self.nums)//2] if len(self.nums) % 2 == 1 else (self.nums[len(self.nums)//2-1]+self.nums[len(self.nums)//2])*0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
