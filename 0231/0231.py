class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        while n>=0:
            if n == 1:
                return True
            elif n < 1:
                return False
            n = n/2

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(-16))
