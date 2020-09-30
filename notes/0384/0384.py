class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums[:]

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp = self.nums[:]
        lo, hi = 0, len(tmp)-1
        while lo < hi:
            idx = random.randint(lo, hi)
            tmp[idx], tmp[hi] = tmp[hi], tmp[idx]
            hi -= 1
        return tmp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
