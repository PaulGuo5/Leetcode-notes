class Solution:
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
    
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        max_pst = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[max_pst] = nums1[i]
                i -= 1
            else:
                nums1[max_pst] = nums2[j]
                j -= 1
            max_pst -= 1
        while i >= 0:
            nums1[max_pst] = nums1[i]
            i -= 1
            max_pst -= 1
        while j >= 0:
            nums1[max_pst] = nums2[j]
            j -= 1
            max_pst -= 1
            
            
    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        nums1[:] = []
        
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[(p1 + p2):] = nums1_copy[p1:]
        if p2 < n:
            nums1[(p1 + p2):] = nums2[p2:]
            
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m-1, n-1
        p = m + n - 1 
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]