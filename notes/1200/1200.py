class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_abs = float('inf')
        res = []
        for i in range(len(arr)-1):
            tmp = arr[i+1] - arr[i] 
            if tmp < min_abs:
                min_abs = tmp
        for i in range(len(arr)-1):
            tmp = arr[i+1] - arr[i]
            if tmp == min_abs:
                res.append([arr[i], arr[i+1]])
        return res
