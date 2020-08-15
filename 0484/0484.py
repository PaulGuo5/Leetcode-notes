class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return None
        nums = [i for i in range(1, len(s)+2)]
        i = 0
        while i < len(s):
            if s[i] == "D":
                j = i
                while i < len(s) and s[i] == "D":
                    i += 1
                nums[j:i+1] = nums[j:i+1][::-1]
                
            else:
                i += 1
        return nums
