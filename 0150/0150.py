class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t in ("+","-","*","/"):
                n2, n1 = int(nums.pop()), int(nums.pop())
                if t == "+":
                    nums.append(n1+n2)
                elif t == "-":
                    nums.append(n1-n2)
                elif t == "/":
                    nums.append(int(n1/n2))
                else:
                    nums.append(n1*n2)
            else:
                nums.append(t)
        return nums[0]
