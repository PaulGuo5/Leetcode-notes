class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.len = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        l = len(word)
        p = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not p.children[index]:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.len = l
    def searchPre(self, word):
        p = self.root
        nodes = []
        for c in word:
            index = ord(c) - ord("a")
            if not p.children[index]:
                return None
            p = p.children[index]
            if p.len != 0:
                return p.len
        return p.len
class Solution:
    def replaceWords(self, dict_: List[str], sentence: str) -> str:
        trie = Trie()
        splited_sentence = sentence.split(" ")
        res = ""
        for word in dict_:
            trie.insert(word)
        for word in splited_sentence:
            if trie.searchPre(word):
                res += word[:trie.searchPre(word)] + " "
            else:
                res += word + " "
        return res[:-1]
