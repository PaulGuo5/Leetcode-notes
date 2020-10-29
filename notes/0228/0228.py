class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        if len(nums) == 1:
            return [str(nums[0])]
        
        res = []
        tmp = [str(nums[0])]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                if len(tmp) > 1:
                    tmp.pop()
                tmp.append(str(nums[i]))
            else:
                if tmp:
                    res.append("->".join(tmp))
                    tmp = [str(nums[i])]
                else:
                    tmp.append(str(nums[i]))
        if tmp:
            res.append("->".join(tmp))
        return res
