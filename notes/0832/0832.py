class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def flip(nums):
            return nums[::-1]
        def invert(nums):
            res = []
            for n in nums:
                res.append(1) if n == 0 else res.append(0)
            return res
        res = []
        for i in A:
            res.append(invert(flip(i)))
        return res
