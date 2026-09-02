class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =1,max(piles)
        res =r
        while l<=r:
            mid = l + (r-l)//2
            totalT =0
            for p in piles:
                totalT += math.ceil(float(p)/mid)
            if totalT <= h :
                res = mid 
                r =mid-1
            else :
                l = mid+1
        
        return res 
