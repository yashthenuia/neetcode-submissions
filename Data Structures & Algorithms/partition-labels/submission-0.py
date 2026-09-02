class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        premap = {}
        for i,c in enumerate(s):
            premap[c] = i
        
        res =[]
        end =0
        ans =0
        for i,c in enumerate(s):
            index = premap[c]
            ans +=1
            end = max(end,index)
            if end==i:
                res.append(ans)
                ans =0
        return res





        