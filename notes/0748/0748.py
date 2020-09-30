class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.replace(" ", "").lower()
        nums = "0123456789"
        for n in nums:
            licensePlate = licensePlate.replace(n, "")
        c = collections.Counter(licensePlate.lower())
        words.sort(key=lambda x:len(x))
        for w in words:
            c_w = collections.Counter(w.lower())
            flag = 0
            for i,j in c.items():
                if c_w[i] < j:
                        flag = 1
            if flag == 0:
                return w
