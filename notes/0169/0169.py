class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        max = 0
        max_num = 0
        for key, value in dic.items():
            if value > max:
                max = value
                max_num = key
        return max_num

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)//2
        return nums[length]