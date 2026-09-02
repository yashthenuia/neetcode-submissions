class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        dp =[float('inf')]*n
        dp[-1]=0
        for i in range(n-2,-1,-1):
            end =min(n, i+nums[i]+1)
            for j in range(i+1,end):
                dp[i] = min(dp[i],1+dp[j])
        return dp[0]
        
        
        # def dfs(i):
        #     if i==n-1:
        #         return 0
        #     if nums[i]==0:
        #         return float('inf')
            
        #     ans =float('inf')
        #     end =min(n, i+nums[i]+1)
        #     for j in range(i+1,end):
        #         ans = min(ans,1+dfs(j))
        #     return ans 
        # return dfs(0)