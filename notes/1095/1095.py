# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def findPeak(mountain_arr):
            lo, hi = 0, mountain_arr.length()-1
            while lo <= hi:
                mi = lo+(hi-lo)//2
                if mountain_arr.get(mi) < mountain_arr.get(mi+1):
                    lo = mi+1
                else: hi = mi-1
            return lo
        
        def findFromSmall(lo, hi, target):
            while lo <= hi:
                mi = lo+(hi-lo)//2
                if mountain_arr.get(mi) == target:
                    return mi
                if mountain_arr.get(mi) < target:
                    lo = mi+1
                else: hi = mi-1
            return -1
        
        def findFromLarge(lo, hi, target):
            while lo <= hi:
                mi = lo+(hi-lo)//2
                if mountain_arr.get(mi) == target:
                    return mi
                if mountain_arr.get(mi) > target:
                    lo = mi+1
                else: hi = mi-1
            return -1
        
        peak = findPeak(mountain_arr)
        l = findFromSmall(0, peak, target)
        if l != -1: return l
        r = findFromLarge(peak+1, mountain_arr.length()-1, target)
        return r
