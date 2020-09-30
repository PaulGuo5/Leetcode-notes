class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        cum = res = 0
        dic = {0:1}
        for num in A:
            cum += num
            diff = cum - S
            if diff in dic:
                res += dic[diff]
            if cum not in dic:
                dic[cum] = 1
            elif cum in dic:
                dic[cum] += 1
        return res