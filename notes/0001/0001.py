class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            r = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == r:
                    res.append(i)
                    res.append(j)
                    return res
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in dic and dic[res] != i:
                return [i, dic[res]]
            else:
                dic[num] = i