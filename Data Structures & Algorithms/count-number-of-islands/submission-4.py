class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        
        def helper(i,j):
            if(i<0 or i>=m or j<0 or j>=n or grid[i][j]=="0"):
                return
            grid[i][j]="0"
            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)
            
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=="1"):
                    count+=1
                    helper(i,j)
        return count
        