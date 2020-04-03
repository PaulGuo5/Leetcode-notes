class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        res = []
        for i, j in cnt.items():
            if i == j:
                res.append(i)
        return max(res) if res else -1
