from functools import cmp_to_key
class Solution:
    def largestNumber1(self, nums: List[int]) -> str:
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
        
        # Build nums contains all numbers in the String format.
        
        nums = list(map(str, nums))
        # nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)
        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'
    
    def merge(self, list1, list2):
        p1, p2 = 0, 0
        result = []
        while p1 < len(list1) and p2 < len(list2):
            if (list1[p1] + list2[p2]) >= (list2[p2] + list1[p1]):
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1
        result += list1[p1:]
        result += list2[p2:]
        return result
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        length = len(nums)
        return self.merge(self.merge_sort(nums[length//2:]), self.merge_sort(nums[:length//2]))
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        return "".join(self.merge_sort(nums)).lstrip("0") or "0"
    
