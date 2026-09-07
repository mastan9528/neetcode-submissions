class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])

        trace = [[0 for i in range(len_col)] for _ in range (len_row)]

        def dfs(row , col):
            if row<0 or col<0 or row>= len_row or col >= len_col or grid[row][col] == "0":
                return
            if grid[row][col]=="1" and trace[row][col]==0:
                trace[row][col] = 1

                dfs(row+1 ,col)
                dfs(row , col+1)
                dfs(row , col-1)
                dfs(row-1 , col)

        cnt = 0

        for i in range(len_row):
            for j in range(len_col):

                if grid[i][j] == "1" and trace[i][j] == 0:
                    print(f" i = {i} , j = {j}")
                    cnt +=1
                    dfs(i , j)

            


        return cnt

        