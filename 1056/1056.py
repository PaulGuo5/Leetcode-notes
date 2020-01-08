class Solution:
    def confusingNumber(self, N: int) -> bool:
        rotated = {6:9, 9:6, 0:0, 1:1, 8:8}
        new = ""
        for i in str(N):
            n = int(i)
            if n in rotated:
                new += str(rotated[n])
            else:
                return False
        if int(new[::-1]) != N:
            return True
        return False
