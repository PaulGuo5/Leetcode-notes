class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        a2z = set('abcdefghijklmnopqrstuvwxyz')
        queue = collections.deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in a2z:
                    if j != word[i]:
                        new = word[:i] + j + word[i+1:]
                        if new in wordList and new not in visited:
                            queue.append((word[:i] + j + word[i+1:], dist+1))
                            visited.add(new)
        return 0
