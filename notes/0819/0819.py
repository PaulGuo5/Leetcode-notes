from collections import Counter
import re
class Solution:
    def mostCommonWord2(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        tmp = ""
        paragraph = paragraph.lower()
        res = []
        for char in paragraph:
            if char >= "a" and char <= "z":
                tmp += char
            else:
                if tmp not in dic:
                    if tmp >= "a" and tmp <= "z":
                        dic[tmp] = 1
                else:
                    dic[tmp] += 1
                tmp = ""
        if tmp:
            if tmp not in dic:
                dic[tmp] = 1
            else:
                dic[tmp] += 1 
        print(dic)
        for char in banned:
            if char not in dic:
                continue
            del dic[char]
        print(dic)
        count = 0
        for key, value in dic.items():
            if value > count:
                count = value
                res = key
        return res
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.split("\W", paragraph)
        count = Counter(words)
        del count[""]
        for char in banned:
            del count[char]
        return max(count, key = lambda k:count[k])
