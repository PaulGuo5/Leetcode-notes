class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        cnt = 0
        dif = []
        rec = set()
        for i in range(len(A)):
            rec.add(A[i])
            if A[i] != B[i]:
                cnt += 1
                dif.append(i)
        if cnt == 0:
            return len(rec) != len(A)
        elif cnt != 2:
            return False
        swap_A = ""
        for i in range(len(A)):
            if i == dif[0]:
                swap_A += A[dif[1]]
            elif i == dif[1]:
                swap_A += A[dif[0]]
            else:
                swap_A += A[i]
        return swap_A == B
