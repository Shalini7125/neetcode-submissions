class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxarea=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count=0
                    count=self.dfs(i,j,grid,m,n)
                    maxarea=max(maxarea,count)
        return maxarea
    def dfs(self,i,j,grid,m,n):
        if i>m-1 or i<0 or j>n-1 or j<0 or grid[i][j]==0:
            return 0
        count=1
        grid[i][j]=0
        count+=self.dfs(i+1,j,grid,m,n)
        count+=self.dfs(i-1,j,grid,m,n)
        count+=self.dfs(i,j+1,grid,m,n)
        count+=self.dfs(i,j-1,grid,m,n)
        return count
                            