"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        lo, hi = 1, z+1
        while 1 <= lo <= z+1 and 1 <= hi <= z+1:
            tmp = customfunction.f(lo, hi)
            if tmp == z:
                res.append([lo, hi])
                lo += 1
                hi -= 1
            elif tmp < z:
                lo += 1
            else:
                hi -= 1
        return res
