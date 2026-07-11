class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i , j = 0 , row*col
        while i<=j:
            mid = i + (j - i)//2
            mid_row = mid//col
            mid_col = mid % col
            if mid_row < row and mid_col < col:
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] > target:
                    j = mid -1
                else:
                    i = mid+1
            else:
                return False
        return False
        