class Solution:
    def prefixesDivBy51(self, A: List[int]) -> List[bool]:
        # exceed time limit
        A = list(map(str, A))
        b = "".join(A)
        m = len(A)
        res = []
        while m > 0:
            tmp = ""
            for i in range(m):
                tmp += b[i]
            if int(tmp, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            m -= 1
        return res[::-1]
    
    
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        # basic dp
        for i in range(1, len(A)):
            # A[i] += A[i - 1] * 2
            A[i] += A[i - 1] * 2 % 5
        return [a % 5 == 0 for a in A]
