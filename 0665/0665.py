class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                flag+=1
                if i == 0:
                    nums[i] = nums[i+1]
                if nums[i+1] <= nums[i-1]:
                    nums[i+1] = nums[i]
                if nums[i+1] > nums[i-1]:
                    nums[i] = nums[i-1]
        if flag > 1:
            return False
        return True
                
