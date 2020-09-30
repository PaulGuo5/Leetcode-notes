class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        sum_ = 0
        res = 0
        for i in arr:
            sum_ += i
            if sum_ > 5000:
                return res
            res += 1
        return res
