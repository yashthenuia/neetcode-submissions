class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        q =deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j,0])
        maxtime =0
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                i,j,time =q.popleft()
                grid[i][j]=2
                
                
                for di,dj in dir:
                    row,col =i+di,j+dj
                    
                    if (0<=row<m and 0<=col<n and grid[row][col]==1):
                        grid[row][col]=2
                        q.append([row,col,time+1])
                maxtime = max(maxtime,time)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return maxtime



            

        