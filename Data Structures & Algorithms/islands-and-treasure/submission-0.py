class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m= len(grid)
        n = len(grid[0])
        dire = [(1,0),(-1,0),(0,1),(0,-1)]
        INF= 2147483647

        def bfs(r,c):
            q = deque([(r,c)])
            visit = [[False]* n for _ in range(m)]
            visit[r][c]=True
            steps =0

            while q:
                for _ in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col]==0:
                        return steps
                    for i,j in dire:
                        ni,nj = row+i,col+j
                        if (0<=ni<m and 0<=nj<n and not visit[ni][nj] and grid[ni][nj]!=-1):
                            visit[ni][nj]=True
                            q.append((ni,nj))
                steps +=1
            return INF
        for i in range(m):
            for j in range(n):
                if grid[i][j]==INF:
                    grid[i][j]= bfs(i,j)

                    
