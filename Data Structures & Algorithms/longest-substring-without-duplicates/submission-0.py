class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp ={}
        ans =0
        l=0
        r=0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1,l)
            mp[s[r]]=r
            ans = max(ans,r-l+1)
        return ans
        