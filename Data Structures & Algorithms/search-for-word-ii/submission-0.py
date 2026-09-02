class TrieNode:
    def __init__(self):
        self.children={}
        self.isword =False
    def addword(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur =cur.children[c]
        cur.isword =True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)
        row,col =len(board),len(board[0])
        res,visit = set(), set()
        def dfs(r,c,node,word):
            if (r <0 or c< 0 or r>=row or c >=col or (r,c) in visit or board[r][c] not in node.children):
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            word +=board[r][c]
            if node.isword:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        
        return list(res)