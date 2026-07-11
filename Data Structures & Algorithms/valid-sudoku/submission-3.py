class Solution:

    def check_element(self,row,col,board,ch)->bool:
        
        for i in range(9):
            if board[i][col] == ch and i != row:
                return False
            if board[row][i] == ch and i != col:
                return False
            r = int(row // 3 * 3 + i // 3)
            c = int(col // 3 * 3 + i % 3)

            if board[r][c] == ch and (r != row or c !=col):
                return False

        return True  
        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_size = len(board)
        row_size = len(board[0])

        for i in range(row_size):
            for j in range(col_size):
                if board[i][j] != ".":
                   flag = self.check_element(i , j , board , board[i][j])
                   if flag == False:
                    return False

        return True
        