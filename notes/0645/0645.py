class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] = -nums[abs(num)-1]
            else:
                res.append(abs(num))
        for i in range(len(nums)):
            if nums[i] >0:
                res.append(i+1)
        return res
