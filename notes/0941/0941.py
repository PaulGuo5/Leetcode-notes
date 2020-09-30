class Solution:
    def validMountainArray1(self, A: List[int]) -> bool:
        # Time limit exceeds
        if len(A) < 3:
            return False
        if sorted(A) == A:
            return False
        for i in range(1, len(A)):
            if sorted(A[:i+1]) == A[:i+1] and sorted(A[i:][::-1]) == A[i:][::-1] and len(set(A[:i+1])) == len(A[:i+1]) and len(set(A[i:][::-1])) == len(A[i:][::-1]):
                return True
        return False
    
    def validMountainArray(self, A: List[int]) -> bool:
        l, r = 0, len(A)-1
        while l+1 < len(A) and A[l+1] > A[l]:
                l += 1
        while r > 0 and A[r-1] > A[r]:
                r -= 1
        return 0 < l==r < len(A)-1
