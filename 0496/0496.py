class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        for c in range(len(nums1)):
            for i in range(len(nums2)):
                if i < len(nums2) and nums1[c] == nums2[i]:
                    for tmp in nums2[i+1:]:
                        if tmp > nums1[c]:
                            res[c] = tmp
                            break
        return res
