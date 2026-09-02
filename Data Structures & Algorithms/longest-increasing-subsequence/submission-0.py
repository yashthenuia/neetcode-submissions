from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[]
        dp.append(nums[0])
        lis =1
        for i in range(1,n):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                lis+=1
                continue
            idx = bisect_left(dp,nums[i])
            dp[idx]= nums[i]

            
        return lis

