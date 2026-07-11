class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        i = 0
        j = (rows * cols)-1

        while i <=j:
            mid = (j+i)//2

            row_ = int(mid / cols)
            col_ = int(mid % cols)

            if matrix[row_][col_]== target:
                return True
            elif matrix[row_][col_] < target:
                i = mid +1
            else:
                j = mid -1

        return False