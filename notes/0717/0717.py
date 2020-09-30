class Solution:
    def isOneBitCharacter1(self, bits: List[int]) -> bool:
        res = []
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                res.append(bits[i])
                i += 1
                continue
            elif bits[i] == 1:
                if i+1 <= len(bits):
                    res.append([bits[i], bits[i+1]])
                    i += 2
                else:
                    return False
        return True if res[-1] == 0 else False
    
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        for i, j in enumerate(bits):
            if j:
                bits.pop(i+1)
        return not j
