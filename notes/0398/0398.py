class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = -1
        cnt = 0
        for i, n in enumerate(self.nums):
            if n == target:
                num = random.randint(0, cnt)
                if num == 0:
                    res = i
                cnt += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
