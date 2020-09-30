class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        cnt_sort = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
        cum = 0
        res = 0
        for i, j in cnt_sort:
            cum += j
            res += 1
            if cum >= len(arr)//2:
                return res
        return res
