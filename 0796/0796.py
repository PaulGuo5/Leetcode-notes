class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        for i in range(len(A)):
            if A[1:]+A[0] == B:
                return True
            else:
                A = A[1:]+A[0]
        return False
