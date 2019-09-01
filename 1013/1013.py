class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        part_sum = sum(A) // 3
        cnt = 0
        total = 0
        for i in A:
            total += i
            if total == part_sum:
                cnt += 1
                total = 0
            print(i, total)
        return cnt == 3
