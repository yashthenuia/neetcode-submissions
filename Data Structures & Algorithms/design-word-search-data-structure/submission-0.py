class Trienode():
    def __init__(self):
        self.children = {}
        self.endofword= False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            
            if w not in cur.children:
                cur.children[w] = Trienode()
            cur = cur.children[w]
        cur.endofword = True

    def search(self, word: str) -> bool:
        def dfs(j,root):

            cur = root
            for w in range(j,len(word)):
                c=word[w]
                if c ==".":
                    for child in cur.children.values():
                        if dfs(w+1,child):
                            return True
                    return False
                else :
                    if c not in cur.children:
                        return False 
                    cur=cur.children[c]
            return cur.endofword
        return dfs(0,self.root)





        
