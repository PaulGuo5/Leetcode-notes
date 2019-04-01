class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        cum = 0
        res = 0
        for num in nums:
            cum += num
            if cum - k in dic:
                res += dic[cum-k]
            if cum in dic:
                dic[cum] += 1
            if cum not in dic:
                dic[cum] = 1
        
        return res