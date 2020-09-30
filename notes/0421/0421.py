class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                j = 1 << i
                tmp = j & num
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
        
        res = 0
        for num in nums:
            node = root
            val = 0
            for i in range(31, -1, -1):
                j = 1 << i
                tmp = j & num
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    val += j
                else:
                    if (node.one and not tmp) or (node.zero and tmp):
                        val += j
                    node = node.one or node.zero
            res = max(res, val)
        return res
