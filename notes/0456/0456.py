class Solution:
    def find132pattern1(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        min_stack = []
        min_tmp = float('inf')
        stack = []
        for n in nums:
            min_tmp = min(min_tmp, n)
            min_stack.append(min_tmp)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_stack[i]:
                while stack and stack[-1] <= min_stack[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
    
    def find132pattern(self, nums: List[int]) -> bool:
        j, stack = -float('inf'), []
        for n in nums[::-1]:
            if n < j: return True
            while stack and stack[-1] < n: j = stack.pop()
            stack.append(n)
        return False
