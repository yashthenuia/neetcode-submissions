class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin=curmax =1
        res =nums[0]

        for i in nums:
            tmp = curmax * i
            curmax = max(tmp,i*curmin,i)
            curmin = min(tmp,i*curmin,i)
            res = max(res,curmax)
        return res
        