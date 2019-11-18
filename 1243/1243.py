class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if len(arr) < 3: return arr
        new = arr[:]
        flag = True
        while flag:
            flag = False
            for i in range(1, len(arr)-1):
                if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                    new[i] = arr[i] - 1
                    flag = True
                elif arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                    new[i] = arr[i] + 1
                    flag = True
            arr = new[:]
        return new
