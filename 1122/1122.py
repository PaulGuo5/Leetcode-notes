class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        dict_1 = {}
        for i in arr1:
            if i not in dict_1: dict_1[i] = 1
            else: dict_1[i] += 1
        for i in arr2:
            if i in set(arr1):
                cnt = dict_1[i]
                while cnt > 0:
                    res.append(i)
                    cnt -= 1
                    dict_1[i] -= 1
        tmp = []
        for i,j in dict_1.items():
            if j > 0:
                while j > 0:
                    tmp.append(i)
                    j -= 1
        return res + sorted(tmp)
        
