class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[0]*m for _ in range(n)]
        def dfs(i,j):
            if i==n-1 or j ==m-1:
                return 1
            if i>= n or j >=m:
                return 0
            if memo[i][j]!=0:
                return memo[i][j]
            memo[i][j] =dfs(i+1,j) + dfs(i,j+1)
            return memo[i][j]
        
        return dfs(0,0)