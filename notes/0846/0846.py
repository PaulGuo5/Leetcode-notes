class Solution:
    def isNStraightHand1(self, hand: List[int], W: int) -> bool:
        hand.sort()
        while hand:
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base+i)
            except:
                return False
        return True
    
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        while hand:
            base = hand[0]
            for i in range(W):
                if base + i not in hand:
                    return False
                hand.remove(base+i)
        return True
