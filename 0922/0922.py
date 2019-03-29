class Solution:
    def sortArrayByParityII2(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        j = 0
        for i in range(0, len(A), 2):
            A[i] = even[j]
            j += 1
        j = 0
        for i in range(1, len(A), 2):
            A[i] = odd[j]
            j += 1
        return A
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1
        while even < len(A) and odd <len(A):
            if A[even] % 2 != 0 and A[odd] % 2 == 0:
                temp = A[even]
                A[even] = A[odd]
                A[odd] = temp
                even += 2
                odd += 2
            elif A[even] % 2 != 0 and A[odd] % 2 != 0:
                odd += 2
            elif A[even] % 2 == 0 and A[odd] % 2 != 0:
                even += 2
                odd += 2
            elif A[even] % 2 == 0 and A[odd] % 2 == 0:
                even += 2
        return A
                