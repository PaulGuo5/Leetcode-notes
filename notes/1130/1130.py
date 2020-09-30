class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        for a in arr:
            while stack[-1] <= a:
                tmp = stack.pop()
                res += tmp*min(a, stack[-1])
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop()*stack[-1]
        return res
