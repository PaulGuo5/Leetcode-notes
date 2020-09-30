class Solution:
    def containsDuplicate2(self, nums: List[int]) -> bool:
        value_set = set()
        for num in nums:
            if num in value_set:
                return True
            else:
                value_set.add(num)
        return False
