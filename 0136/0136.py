# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
class Solution:
	def singleNumber(self,nums):
		for i in nums:
			dic = {}
			for i in nums:
				if i not in dic:
					dic[i]=1
				else:
					dic[i]=2
			for j in nums:
				if dic[j]==1:
					return j
	def singleNumber2(self,nums):
		nums.sort()
		for i in range(0,len(nums)-1,2):
			if nums[i]!=nums[i+1]:
				return nums[i]
		return nums[-1]
if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([4,1,2,1,2]))
    print(solution.singleNumber2([4,1,2,1,2]))
    

