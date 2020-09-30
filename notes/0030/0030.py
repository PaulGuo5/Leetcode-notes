class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        res = []
        word_len = len(words[0])
        window = len(words)*word_len
        cnt = collections.Counter(words)
        for i in range(len(s)-window+1):
            tmp = collections.defaultdict(int)
            for j in range(i, i+window, word_len):
                w = s[j: j+word_len]
                if w in cnt:
                    tmp[w] += 1
                    if tmp[w] > cnt[w]:
                        break
                else:
                    break
                if tmp == cnt:
                    res.append(i)
        return res
