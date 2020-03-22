class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for c in dict:
            self.d.add(c)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for idx in range(len(word)):
            for i in range(26):
                sub = chr(ord('a') + i)
                if sub == word[idx]:
                    continue
                new_word = word[:idx] + sub + word[idx + 1:]
                if new_word in self.d:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
