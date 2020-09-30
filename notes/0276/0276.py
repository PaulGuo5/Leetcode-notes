class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0

        num_same = 0 # the number of ways that the last element has the same color as the second last one
        num_diff = k # the number of ways that the last element has differnt color from the second last one

        for i in range(1, n):
            total = num_diff + num_same
            num_same = num_diff
            num_diff = total * (k - 1)

        return num_same + num_diff
