from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(Counter, (nums1, nums2))
        return list((a & b).elements())
