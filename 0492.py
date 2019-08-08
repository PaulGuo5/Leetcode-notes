class Solution:
    def constructRectangle1(self, area: int) -> List[int]:
        # time limit exceeded
        all_LW = []
        diff_min = float("inf")
        res = []
        for L in range(1, area+1):
            if area % L == 0:
                W = area // L
                if W <= L:
                    all_LW.append([L, W])
        print(all_LW)
        for i in all_LW:
            diff = i[0] - i[1]
            if diff < diff_min:
                res = i
                diff_min = diff
        return res
    
    def constructRectangle(self, area: int) -> List[int]:
        W = int(math.sqrt(area))
        while area % W:
            W -= 1
        return [ area//W, W ]
