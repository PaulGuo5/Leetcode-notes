class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def get_char_len_nxtNondulpicatedIdx(word, cur_idx):
            length = 1
            for i in range(cur_idx+1, len(word)):
                if word[i] != word[cur_idx]:
                    return word[cur_idx], length, i
                length += 1
            return word[cur_idx], length, len(word)
        
        def check(s, word):
            ids, idw = 0, 0
            while ids < len(s) and idw < len(word):
                s_cur_word, s_length, ids = get_char_len_nxtNondulpicatedIdx(s, ids)
                w_cur_word, w_length, idw = get_char_len_nxtNondulpicatedIdx(word, idw)
                if s_cur_word != w_cur_word:
                    return 0
                if s_length < w_length:
                    return 0
                if s_length == 2 and w_length == 1:
                    return 0
            if ids == len(s) and idw == len(word):
                return 1
            return 0
        
        res = 0
        for w in words:
            res += check(S, w)
        return res
