class Solution:
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target in row:
                return True
        return False

    
    def searchMatrix(self, matrix, target):
        def binary_search(matrix, target, start, v):
            lo = start
            hi = len(matrix[0])-1 if v else len(matrix) - 1
            
            while lo <= hi:
                mid = (lo+hi) // 2
                if v:
                    if matrix[start][mid] < target:
                        lo = mid + 1
                    elif matrix[start][mid] > target:
                        hi = mid - 1
                    else:
                        return True
                else:
                    if matrix[mid][start] < target:
                        lo = mid + 1
                    elif matrix[mid][start] > target:
                        hi = mid - 1
                    else:
                        return True
            return False
        
        if not matrix:
            return False
        for i in range(min(len(matrix), len(matrix[0]))):
            v_found = binary_search(matrix, target, i, True)
            h_found = binary_search(matrix, target, i, False)
            if v_found or h_found:
                return True
        return False
