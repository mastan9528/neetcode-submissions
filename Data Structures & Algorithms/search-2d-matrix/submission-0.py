class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        row = len(matrix)
        col = len(matrix[0])
        j = (row * col)-1

        while i <= j :
            mid = int((i+j)/2)
            row_ = int(mid/col)
            col_ = int(mid % col)
            if matrix[row_][col_] == target:
                return True
            elif matrix[row_][col_] < target:
                i = mid+1
            else:
                j = mid-1

        return False
        