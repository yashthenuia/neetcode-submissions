class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        st= 0
        rt=n-1
        while(st <= rt):
            md =rt +  ((st -rt)//2)
            if nums[md] == target:
                return md
            elif nums[md] < target:
                st = md+1
            else :
                rt =md -1
        return -1