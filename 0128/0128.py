class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, d = 0, {}
        for n in nums:
            if n not in d:
                left = d.get(n-1, 0)
                right = d.get(n+1, 0)
                
                l = left+right+1
                res = max(res, l)
                
                d[n] = l
                d[n-left] = l
                d[n+right] = l

        return res
