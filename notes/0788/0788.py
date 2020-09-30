class Solution:
    def rotatedDigits(self, N: int) -> int:
        def rotated(d):
            if d == 0 or d == 1 or d == 8:
                return d
            elif d == 2 or d == 5:
                return 2 if d == 5 else 5
            elif d == 6 or d == 9:
                return 6 if d == 9 else 9
            else:
                return -1

        def isRotated(n):
            res = ""
            for d in str(n):
                if rotated(int(d)) == -1:
                    return False
                res += str(rotated(int(d)))
            return False if int(res) == n else True
        cnt = 0
        for i in range(1, N+1):
            if isRotated(i):
                cnt+=1
        return cnt
