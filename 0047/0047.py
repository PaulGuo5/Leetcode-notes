class Solution:
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(first):
            if first == len(nums):
                if nums[:] not in res:
                    res.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack(0)
        return res
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def backtrack(first):
            if first == len(nums):
                s = ''.join([str(x) for x in nums[:]])
                if s not in used:
                    used.add(s)
                    res.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack(0)
        return res
