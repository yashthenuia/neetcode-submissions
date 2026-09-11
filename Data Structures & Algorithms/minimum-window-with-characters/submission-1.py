class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        dic = {}
        for i in t:
            dic[i] = dic.get(i,0) +1
        need = len(dic)
        counts = {}
        have =0
        l=0
        ans =100000
        res =[-1,-1]
        for j in range(len(s)):
            counts[s[j]] = counts.get(s[j],0) +1
            if s[j] in dic and dic[s[j]] == counts[s[j]]:
                have +=1
            while have ==need:
                if ans > (j-l+1):
                    ans = j-l+1
                    res =[l,j]
                counts[s[l]] -=1
                if s[l] in dic and counts[s[l]] < dic[s[l]]:
                    have -=1
                l +=1
        return s[res[0]:res[1]+1] if ans !=100000 else ""
