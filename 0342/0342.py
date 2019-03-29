class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        else:
            while num>=0:
                if num == 1:
                    return True
                elif num < 1:
                    return False
                num /= 4
if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfFour(20))