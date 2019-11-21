class Solution:
    def isArmstrong(self, N: int) -> bool:
        sum_ = 0
        for i in str(N):
            sum_ += int(i)**len(str(N))
        return sum_ == N
