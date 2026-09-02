class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        coins.sort()
        memo = [[-1] *(amount+1) for _ in range(len(coins)+1)]

        def dfs(i,value):
            if value==0:
                return 1
            if value < 0:
                return 0
            if memo[i][value]!=-1:
                return memo[i][value]
            ans =0
            for k in range(i,len(coins)):
                if value-coins[k] >=0:
                    ans +=dfs(k,value-coins[k])
            memo[i][value]=ans 
            return ans 
        

        return dfs(0,amount)