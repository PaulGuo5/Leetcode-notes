class Solution:
    def findSpecialInteger1(self, arr: List[int]) -> int:
        n = len(arr) // 4
        cnt = collections.Counter(arr)
        for i, j in cnt.items():
            if j > n:
                return i
        return None
    
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        n = len(arr) // 4
        j = 1
        pre = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == pre:
                j += 1
                if j > n:
                    return arr[i]
            else:
                j = 1
                pre = arr[i]
