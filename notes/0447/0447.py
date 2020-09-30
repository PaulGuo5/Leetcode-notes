class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p1 in points:
            dict_p = {}
            for p2 in points:
                dist = (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2
                if dist not in dict_p:
                    dict_p[dist] = 1
                else:
                    dict_p[dist] += 1
            for d in dict_p:
                res += dict_p[d] * (dict_p[d]-1)
        return reso

