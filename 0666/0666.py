class Solution:
    def pathSum(self, nums: List[int]) -> int:
        table = {}
        for n in nums:
            hundreds, tens, units = n // 100, (n // 10)%10, n % 10
            if (hundreds, tens) not in table:
                table[(hundreds, tens)] = units + table.get((hundreds-1, (tens+1)//2), 0)
            else:
                table[(hundreds, tens)] += units + table.get((hundreds-1, (tens+1)//2), 0)
        
        res = 0
        for depth, pos in table.keys():
            if (depth+1, pos*2-1) not in table and (depth+1, pos*2) not in table:
                res += table[(depth, pos)]
        return res
