class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(word, 0, self.root)
    
    def match(self, word, index, root):
        if root == None:
            return False
        if index == len(word):
            return root.is_word
        if word[index] != ".":
            if word[index] in root.children:
                return self.match(word, index + 1, root.children[word[index]])
        else:
            for child in root.children.values():
                if self.match(word, index + 1, child):
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
