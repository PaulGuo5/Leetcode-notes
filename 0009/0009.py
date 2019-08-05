class Solution:
    def isPalindrome(self, x: int) -> bool:
        left, right = 0, len(str(x))-1
        while left < right:
            if str(x)[left] != str(x)[right]:
                return False
            left += 1
            right -= 1
        return True
