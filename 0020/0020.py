class Solution:
    def isValid(self, s: str) -> bool:
        labels = {"(":")","{":"}","[":"]"}
        stack = []
        for label in s:
            if label in labels.keys():
                stack.append(label)
            else:
                # if not stack or label != labels[stack[-1]]:
                #     return False
                # else:
                #     stack.pop()
                if not stack or label != labels[stack.pop()]:
                    return False
        if stack:
            return False
        return True
