class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        dic = {}
        res = []
        nums_sort = sorted(nums, reverse = True)
        for i,j in enumerate(nums_sort):
            for n in nums:
                if n == j:
                    dic[n] = i+1
        for n in nums:
            if dic[n] == 1:
                res.append("Gold Medal")
            elif dic[n] == 2:
                res.append("Silver Medal")
            elif dic[n] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(dic[n]))
        return res
