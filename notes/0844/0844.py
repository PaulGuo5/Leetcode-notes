class Solution:
    def backspace(self, s):
        stack = []
        if not s:
            return s
        for char in s:
            if char == "#":
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(char)
        return stack
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.backspace(S)
        T = self.backspace(T)
        if S == T:
            return True
        return False
