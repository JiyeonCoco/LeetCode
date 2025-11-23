class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_first = 0
        row_last = len(matrix)-1

        while row_first <= row_last:
            row_mid = (row_first+row_last) // 2

            if matrix[row_mid][0] == target:
                return True
            elif matrix[row_mid][0] < target:
                row_first = row_mid + 1
            else:
                row_last = row_mid - 1

        
        col_first = 0
        col_last = len(matrix[0])-1

        while col_first <= col_last:
            col_mid = (col_first+col_last) // 2

            if matrix[row_last][col_mid] == target:
                return True
            elif matrix[row_last][col_mid] < target:
                col_first = col_mid + 1
            else:
                col_last = col_mid - 1

        return False
