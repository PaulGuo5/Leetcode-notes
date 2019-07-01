from collections import Counter
class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        nums_map = Counter(nums)
        res_list = nums_map.most_common(k)
        res = []
        for i in res_list:
            res.append(i[0])
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = Counter(nums)
        nums_sorted = sorted(nums_map.items(), key = lambda x: x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(nums_sorted[i][0])
        return res
