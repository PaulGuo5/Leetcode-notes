from collections import Counter
class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(Counter, (nums1, nums2))
        return list((a & b).elements())
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1)&Counter(nums2)).elements())
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2.sort()
        for i in nums1:
            flag, j = self.binarySearch(nums2, i)
            if flag:
                res.append(i)
                del nums2[j]
        return res
    def binarySearch(self, nums, t):
        low, high = 0 ,len(nums)
        while low < high:
            mid = (low+high) // 2
            if nums[mid] == t:
                return True, mid
            elif nums[mid] < t:
                low = mid + 1
            else:
                high = mid
        return False, -1
