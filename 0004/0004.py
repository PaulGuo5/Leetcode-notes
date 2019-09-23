class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        return self.findKth(nums1, nums2, l//2) if l%2 == 1 else ((self.findKth(nums1, nums2, l//2-1)+self.findKth(nums1, nums2, l//2))*0.5)
    
    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            return nums2[k]
        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])
        i = len(nums1) // 2
        j = k - i
        if nums1[i] > nums2[j]:
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)
        
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (l1 + l2 + 1) // 2
        low, hig = 0, l1
        while low < hig:
            m1 = (low + hig) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                low = m1 + 1
            else:
                hig = m1
        
        m1 = low
        m2 = k - low
        n_m1_1 = -float('inf') if m1 <= 0 else nums1[m1-1]
        n_m2_1 = -float('inf') if m2 <= 0 else nums2[m2-1]
        c1 = max(n_m1_1, n_m2_1)
        
        if (l1+l2) % 2 == 1:
            return c1
        
        n_m1 = float('inf') if m1 >= l1 else nums1[m1]
        n_m2 = float('inf') if m2 >= l2 else nums2[m2]
        c2 = min(n_m1, n_m2)
        
        return (c1+c2) * 0.5
