class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minnum = arrays[0][0]
        maxnum = arrays[0][-1]
        maxdiff = float('-inf')
        
        for array in arrays[1:]:
            maxdiff = max(maxdiff, array[-1]-minnum, maxnum-array[0])
            minnum = min(minnum, array[0])
            maxnum = max(maxnum, array[-1])
        
        return maxdiff
