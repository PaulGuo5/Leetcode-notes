class Solution:
    def maxArea(self, height: List[int]) -> int:
        fst = 0
        lst = len(height)-1
        res = 0
        while fst < lst:
            if height[fst] > height[lst]:
                res = max(res, height[lst] * (lst-fst))
                lst -= 1
            else:
                res = max(res, height[fst] * (lst-fst))
                fst += 1
        return res