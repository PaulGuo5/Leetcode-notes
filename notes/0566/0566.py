import numpy as np
class Solution:
    def matrixReshape1(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]):
            return nums
        nums = np.array(nums)
        return nums.reshape(r,c)
    
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]):
            return nums
        new_nums = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                new_nums.append(nums[i][j])
        res = [[None]*c for i in range(r)]
        k=0
        for i in range(r):
            for j in range(c):
                res[i][j] = new_nums[k]
                k+=1
        return res
