class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for w in words:
            tmp = ""
            for c in w:
                tmp += morse[ord(c) - ord("a")]
            res.add(tmp)
        return len(res)
