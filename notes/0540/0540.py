class Solution:
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        for i, j in collections.Counter(nums).items():
            if j == 1:
                return i
            
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N-1
        while l <= r:
            if l == r :return nums[l]
            m = (l+r) // 2
            if 0 < m < N-1 and nums[m-1] != nums[m] and nums[m] != nums[m+1]:
                return nums[m]
            if m%2:
                if nums[m] == nums[m-1]:
                    l = m+1
                else:
                    r = m-1
            else:
                if nums[m] == nums[m-1]:
                    r = m-2
                else:
                    l = m+2
            
        return nums[l]
