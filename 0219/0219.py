class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_dict = {}
        for i in range(len(nums)):
            if nums[i] in value_dict and abs(value_dict[nums[i]] - i) <= k:
                return True
            value_dict[nums[i]] = i
        return False
