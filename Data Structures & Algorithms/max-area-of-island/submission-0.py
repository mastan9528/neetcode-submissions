class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])

        def dfs(row , col):
            if row<0 or col<0 or row>= len_row or col >= len_col or grid[row][col] == 0:
                return 0
            
            grid[row][col]=0
            return(
                1
                +dfs(row+1 ,col )
                +dfs(row , col+1)
                +dfs(row , col-1)
                +dfs(row-1 , col)
            )
            

        maxi = 0
        for i in range(len_row):
            for j in range(len_col):

                if grid[i][j] == 1:
                    print(f" i = {i} , j = {j}")
                    
                    maxi = max(maxi , dfs(i , j))

            


        return maxi
        