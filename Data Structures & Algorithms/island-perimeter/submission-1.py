class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visit=set()
        def helper(i,j):
            if(i<0 or i>=m or j<0 or j>=n or grid[i][j]==0):
                return 1
            if((i,j) in visit):
                return 0
            visit.add((i,j))
            return helper(i+1,j)+helper(i-1,j)+helper(i,j+1)+helper(i,j-1)
        for i in range(m):
            for j in range(n):
                if(grid[i][j]):
                    return helper(i,j)





        