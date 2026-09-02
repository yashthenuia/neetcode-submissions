class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>= col or board[i][j]!="O":
                return
            
            board[i][j]="Y"
                
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(row):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][col-1]=="O":
                dfs(i,col-1)
        for i in range(col):
            if board[0][i]=="O":
                dfs(0,i)
            if board[row-1][i]=="O":
                dfs(row-1,i)
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
        for i in range(row):
            for j in range(col):
                if board[i][j]=="Y":
                    board[i][j]="O"
         

        