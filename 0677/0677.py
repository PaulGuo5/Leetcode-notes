# class TrieNode:
#     def __init__(self):
#         self.children = [None]*26
#         self.value = 0
#         self.sum = 0
# class MapSum:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()

#     def insert(self, key: str, val: int) -> None:
#         p = self.root
#         nodes = []
#         for c in key:
#             index = ord(c) - ord("a")
#             if not p.children[index]:
#                 p.children[index] = TrieNode()
#             p = p.children[index]
#             nodes.append(p)
#         if p.value != val:
#             delta = val - p.value
#             p.value = val
#             for node in nodes:
#                 node.sum += delta
            
#     def sum(self, prefix: str) -> int:
#         p = self.root
#         for c in prefix:
#             index = ord(c) - ord("a")
#             if not p.children[index]:
#                 return 0
#             p = p.children[index]
#         return p.sum
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.sum = 0
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        p = self.root
        nodes = []
        for c in key:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
            nodes.append(p)
        if p.value != val:
            delta = val - p.value
            p.value = val
            for node in nodes:
                node.sum += delta
            
    def sum(self, prefix: str) -> int:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return 0
            p = p.children[c]
        return p.sum
