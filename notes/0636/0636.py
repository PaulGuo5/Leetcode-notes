class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        for log in logs:
            idx, op, time = log.split(":")
            idx, time = int(idx), int(time)
            if op == "start":
                if stack:
                    res[stack[-1][0]] += time - stack[-1][1]
                stack.append([idx, time])
            else:
                prev = stack.pop()
                res[prev[0]] += time - prev[1] + 1
                if stack:
                    stack[-1][1] = time + 1
        return res
