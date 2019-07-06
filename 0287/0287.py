from collections import Counter
class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        nums_map = Counter(nums)
        for i, j in nums_map.items():
            if j > 1:
                return i
    def findDuplicate2(self, nums: List[int]) -> int:
        low ,high = 1, len(nums)
        while low < high:
            mid = (low + high) // 2
            if mid < sum(x <= mid for x in nums):
                high = mid
            else:
                low = mid + 1
        return low
    def findDuplicate3(self, nums: List[int]) -> int:
        finder, slow, fast = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                return slow
            
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        finder = 0
        while slow != finder:
            slow = nums[slow]
            finder = nums[finder]
        return slow
