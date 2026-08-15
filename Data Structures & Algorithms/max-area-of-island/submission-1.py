class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxarea=0
        def helper(i,j):
            if(i>=m or i<0 or j<0 or j>=n or grid[i][j]==0):
                return 0
            grid[i][j]=0
            return 1+helper(i-1,j)+helper(i+1,j)+helper(i,j-1)+helper(i,j+1)
        for i in range(m):
            for j in range(n):
                if(grid[i][j]):
                    maxarea=max(maxarea,helper(i,j))
        return maxarea
        