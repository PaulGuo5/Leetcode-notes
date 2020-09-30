class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        if cnt[0] >= 2: return True
        table = set(arr)
        for n in arr:
            if 2*n in table and n != 2*n:
                return True
        return False
