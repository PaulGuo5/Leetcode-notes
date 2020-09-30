class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        cnt = set()
        for i, j in c.items():
            if j in cnt:
                return False
            cnt.add(j)
        return True
