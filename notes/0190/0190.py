class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        # n=int(n)
        for i in range(32):
            res += 1 & n
            if i == 31:
                return res
            n >>= 1
            res <<= 1



if __name__ == '__main__':
	solution = Solution()
	print(solution.reverseBits("00000010100101000001111010011100"))