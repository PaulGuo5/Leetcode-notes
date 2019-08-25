class Solution:
    def binaryGap(self, N: int) -> int:
        b = bin(N)[2:]
        dis = 0
        pre = 0
        for i in range(len(b)):
            if b[i] == "1":
                dis = max(dis, i - pre)
                pre = i
        return dis
