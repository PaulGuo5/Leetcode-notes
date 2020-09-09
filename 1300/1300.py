class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = []
        cum = 0
        min_diff = float('inf')
        res = 0
        for i in arr:
            cum += i
            prefix.append(cum)
        for v in range(0, arr[-1]+1):
            idx = bisect.bisect_right(arr, v)
            amount = v*(n-idx)
            if idx-1 >= 0:
                amount += prefix[idx-1]
            if min_diff > abs(amount-target):
                min_diff = abs(amount-target)
                res = v
        return res
