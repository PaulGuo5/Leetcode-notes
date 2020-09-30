# class TrieNode:
#     def __init__(self):
#         self.is_word = False
#         self.children = [None]*26
# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         p = self.root
#         for c in word:
#             index = ord(c) - ord("a")
#             if not p.children[index]:
#                 p.children[index] = TrieNode()
#             p = p.children[index]
#         p.is_word = True

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         return self.find(word) and self.find(word).is_word

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         return self.find(prefix) 
        
#     def find(self, word):
#         p = self.root
#         for c in word:
#             index = ord(c) - ord("a")
#             if not p.children[index]:
#                 return None
#             p = p.children[index]
#         return p

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.find(word) and "#" in self.find(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix) 
        
    def find(self, word):
        p = self.root
        for c in word:
            if c not in p:
                return None
            p = p[c]
        return p
