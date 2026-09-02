class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        dict[nums[0]]=0
        ans =[]
        for i in range(1,len(nums)):
            check = target - nums[i]
            if check in dict:
                ans.append(dict[check])
                ans.append(i)
                return ans
            dict[nums[i]]=i
            
        

        
        