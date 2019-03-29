class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            # carry, digits[i] = divmod(digits[i]+carry, 10)
            carryPre = carry
            carry = (digits[i] + carryPre) // 10
            digits[i] = (digits[i]+carryPre) % 10
            if carry == 0:
                return digits
        return [1]+digits