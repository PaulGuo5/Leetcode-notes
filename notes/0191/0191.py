# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n = str(bin(n))
        n = str(n)
        count = 0
        for i in n:
        	if i == "1":
        		count=count+1
        return count
    def hammingWeight2(self, n):
    	count=0
    	while n:
            count += n&1
            n/=2
    	return count

if __name__ == '__main__':
	solution = Solution()
	print(solution.hammingWeight("00000000000000000000000000001011"))
	# print(solution.hammingWeight2("00000000000000000000000000001011"))
