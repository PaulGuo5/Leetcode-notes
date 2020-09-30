class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0
        table = {0:0}
        res = 0
        for i, n in enumerate(nums, 1):
            if n == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt in table:
                res = max(res, i - table[cnt])
            else:
                table[cnt] = i
                
        return res
