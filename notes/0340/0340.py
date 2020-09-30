class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0
        d = collections.defaultdict(int)
        while right < len(s):
            d[s[right]] = right
            right += 1
            if len(d) > k:
                del_ind = min(d.values())
                del d[s[del_ind]]
                left = del_ind + 1
            res = max(res, right-left)
        return res
