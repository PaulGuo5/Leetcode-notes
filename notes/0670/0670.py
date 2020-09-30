class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [i for i in str(num)]
        last = {int(x): i for i, x in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(9, int(nums[i]), -1):
                if last.get(j,0) > i:
                    nums[last[j]], nums[i] = nums[i], nums[last[j]]
                    return int("".join(nums))
        return num
