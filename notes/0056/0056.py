class Solution:
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        res = []
        points = []
        for interval in intervals:
            points.append([interval[0], 0])
            points.append([interval[1], 1])
        points.sort()
        for i,j in points:
            if not j:
                stack.append(i)
            else:
                start = stack.pop()
                if not stack:
                    res.append([start, i])
        return res
    
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        stack = []
        intervals.sort()
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if stack[-1][1] >= interval[0]:
                    pre = stack.pop()
                    stack.append([pre[0], max(pre[1], interval[1])])
                else:
                    stack.append(interval)
        return stack
