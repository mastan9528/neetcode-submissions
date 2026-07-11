class Solution:
    def checking(self , ch , row, col, board):
        for i in range(9):
            if board[row][i] == ch and col != i:
                return False
            if board[i][col] == ch and row != i:
                return False
            x = int(((row // 3)*3) + i // 3)
            y = int(((col // 3)*3) + i % 3)
            

            if board[x][y] == ch and (x != row or y != col):
                return False
        return True




    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    bo = self.checking(board[i][j],i , j , board)
                    if bo == False:
                        return False
        return True
        