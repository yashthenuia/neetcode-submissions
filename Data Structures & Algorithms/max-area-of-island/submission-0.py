class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit=set()
        ans =0
        def dfs(i,j):
            
            if i<0 or i>=rows or j <0 or j>= cols or grid[i][j]==0 or (i,j) in visit:
                return 0
            
            visit.add((i,j))
            return (1+dfs(i+1,j) + dfs(i-1,j) +dfs(i,j+1)+dfs(i,j-1))
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    ans = max(ans,dfs(i,j)) 
        return ans

