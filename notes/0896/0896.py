class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A:
            return True
        elif len(A)==1:
            return True
        else:
            preFlag = 0
            for i in range(len(A)-1):
                if A[i] == A[i+1]:
                    continue
                if A[i] > A[i+1]:
                    flag = -1
                    if preFlag == 0:
                        preFlag = flag
                    elif flag != preFlag:
                        return False
                    else:
                        preFlag = flag
                if A[i] < A[i+1]:
                    flag = 1
                    if not preFlag:
                        preFlag = flag
                    elif flag != preFlag:
                        return False
                    else:
                        preFlag = flag
        return True
        
        # inc, dec = False, False
        # for i in range(len(A)-1):
        #     if A[i] < A[i+1]:
        #         inc = True
        #     if A[i] > A[i+1]:
        #         dec = True
        # return not inc or not dec