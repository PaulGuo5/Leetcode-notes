class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        def findUncommon(a_cnt, b_cnt):
            uncommon_words = set()
            for i,j in a_cnt.items():
                if j == 1 and not b_cnt[i]:
                    uncommon_words.add(i)
            return uncommon_words
        A = A.split(" ")
        B = B.split(" ")
        a_cnt = collections.Counter(A)
        b_cnt = collections.Counter(B)
        return list(findUncommon(a_cnt, b_cnt) | findUncommon(b_cnt, a_cnt))
