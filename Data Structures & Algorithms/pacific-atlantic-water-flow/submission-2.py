class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row =len(heights)
        col = len(heights[0])
        
        pac ,atl =set(),set()

        def dfs(i,j,visit,preval):
            if ((i,j) in visit or i<0 or j<0 or i==row or j ==col or heights[i][j] < preval):
                return 
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
        res =[]
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

            
        return res


        