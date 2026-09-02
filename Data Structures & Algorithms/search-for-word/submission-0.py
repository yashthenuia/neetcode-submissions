class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordmap = []
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            wordmap.append([False]*m)
        
              

        def dfs(i,j,l,wordmap):
            if l ==len(word):
                return True 
            xt =[1,-1,0,0]
            yt =[0,0,1,-1]
            for k in range(4):
                if i+xt[k]>=0 and i+xt[k]<n and j+yt[k] >=0 and j+yt[k] <m:

                    if ( board[i+xt[k]][j+yt[k]]==word[l] and not wordmap[i+xt[k]][j+yt[k]]):
                        wordmap[i+xt[k]][j+yt[k]]=True
                        if dfs(i+xt[k],j+yt[k],l+1,wordmap):
                            return True 
                        wordmap[i+xt[k]][j+yt[k]]=False

            return False  
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    wordmap[i][j]=True
                    val = dfs(i,j,1,wordmap)

                    if val ==True:
                        return True
                    wordmap[i][j]=False
        return False 
        