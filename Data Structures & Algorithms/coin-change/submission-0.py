class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo ={}
        if amount ==0:
            return 0
        def dfs(value):
            
            if value ==0:
                return 0
            if value in memo:
                return memo[value] 
            ans =float('inf')
            for i in coins:
                if value - i>= 0:
                    ans = min(ans,1+ dfs(value-i))
            memo[value]=ans
            return memo[value]
        res = dfs(amount)
        if res !=float('inf'):
            return res
        return -1