class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1

                    self.dfs(i,j,grid,m,n)
        return count
    def dfs(self,i,j,grid,m,n):
        if i>m-1 or j>n-1 or j<0 or i<0 or grid[i][j]=='0':
            return
        grid[i][j]='0'
        self.dfs(i+1,j,grid,m,n)
        self.dfs(i-1,j,grid,m,n)
        self.dfs(i,j+1,grid,m,n)
        self.dfs(i,j-1,grid,m,n)
    
        