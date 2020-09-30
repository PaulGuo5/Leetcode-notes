class Solution:
    def peakIndexInMountainArray1(self, A: List[int]) -> int:
        low, high = 0, len(A)-1
        while low < high:
            mid = (low+high) // 2
            if A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid    
        return low
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A)-1
        while low <= high:
            mid = (low+high) // 2
            if A[mid] < A[high]:
                low = mid + 1
            elif A[mid] < A[high]:
                high = mid
            else:
                high -= 1
        return low
