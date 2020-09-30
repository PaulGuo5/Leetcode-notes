class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        stack = [[1,""]]
        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                stack.append([int(num),""])
                num = ""
            elif char == "]":
                n, string = stack.pop()
                stack[-1][1] += string * n
            else:
                stack[-1][1] += char
        return stack[-1][1]
