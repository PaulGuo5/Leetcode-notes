class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = collections.Counter(A)
        for i,j in c.items():
            if j == len(A)//2:
                return i
