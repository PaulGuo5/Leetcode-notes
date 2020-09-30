class FenwickTree:
    def __init__(self, n):
        self.prefixSum = [0]*(n+1)
        self.n = len(self.prefixSum)
        
    def update(self, i, diff):
        while i < self.n:
            self.prefixSum[i] += diff
            i += i & -i
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.prefixSum[i]
            i -= i & -i
        return s
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ft = FenwickTree(len(self.nums))
        for i, n in enumerate(self.nums):
            self.ft.update(i+1, n)

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.ft.update(i+1, delta)
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.ft.query(j+1) - self.ft.query(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
