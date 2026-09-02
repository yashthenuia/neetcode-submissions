class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countt , counts = {},{}
        for i in t:
            countt[i]= 1 +countt.get(i,0)
        
        need = len(countt)
        res = [-1,-1]
        reslen = 100000
        have = 0
        l = 0
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)

            if s[i] in countt and countt[s[i]] == counts[s[i]]:
                have += 1
            while have == need:
                if reslen > (i - l + 1):
                    reslen = i - l + 1
                    res = [l, i]
                
                counts[s[l]] -= 1
                if s[l] in countt and counts[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1]+1] if reslen != 100000 else ""