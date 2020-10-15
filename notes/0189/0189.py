class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        n = len(nums)
        k %= n
        
        def reverse(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
        
        reverse(0, n-k-1)
        reverse(n-k, n-1)
        reverse(0, n-1)
