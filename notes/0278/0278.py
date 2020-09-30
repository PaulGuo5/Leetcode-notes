# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion1(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        res = []
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                res.append(mid)
                high = mid - 1
            else:
                low = mid + 1
        return min(res)
    
    def firstBadVersion(self, n):
        low, high = 0, n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid-1
            else:
                low = mid+1
        return low
