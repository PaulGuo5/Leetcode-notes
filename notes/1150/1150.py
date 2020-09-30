class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return False
        c = collections.Counter(nums)
        max_ = -float('inf')
        for i, j in c.items():
            if j > max_:
                max_ = j
        if max_ > len(nums) // 2:
            return True
        return False
