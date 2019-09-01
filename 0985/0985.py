class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_ = sum([a for a in A if a%2 == 0])
        res = []
        for q in queries:
            if A[q[1]] % 2 == 0:
                sum_ -= A[q[1]]
            A[q[1]] += q[0]
            if A[q[1]] % 2 == 0:
                sum_ += A[q[1]]
            res.append(sum_)
        return res
