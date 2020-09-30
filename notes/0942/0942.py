class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        nums, res = [], []
        for i in range(len(S)+1):
            nums.append(i)
        for s in S:
            if s == "I":
                res.append(nums.pop(0))
            else:
                res.append(nums.pop())
        return res+nums
