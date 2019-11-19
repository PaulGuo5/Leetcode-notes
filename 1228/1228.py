class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0])//(len(arr))
        for x, y in zip(arr[1:], arr):
            if x - y != diff:
                return y + diff
        return diff
