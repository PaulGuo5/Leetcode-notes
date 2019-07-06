from collections import defaultdict
class Solution:
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        d = defaultdict(list)
        res = []
        for i in arr:
            d[abs(i-x)] += [i]
        print(d)
        for i in sorted(d.keys()):
            res += d[i]
        return sorted(res[:k])
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0 ,len(arr) - k
        while low < high:
            mid = (low+high) // 2
            if x - arr[mid] > arr[mid+k] - x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]
