class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # return [i for i, j in collections.Counter(nums).items() if j == 1]
        tmp = 0
        for n in nums:
            tmp ^= n
        tmp = tmp & -tmp
        res1, res2 = 0, 0
        for n in nums:
            if n & tmp:
                res1 ^= n
            else:
                res2 ^= n
        return [res1, res2]