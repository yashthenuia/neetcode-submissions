class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}

        def dfs(i):
            if i > len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
            rob = nums[i] + dfs(i+2)
            notrob = dfs(i+1)
            memo[i]= max(rob,notrob)
            return memo[i]
        return dfs(0)


        