class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start =0
        mid =0
        end =n-1
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while mid <= end:
            if nums[mid]==0:
                swap(start,mid)
                start +=1
            elif nums[mid]==2:
                swap(mid,end)
                end -=1
                mid -=1
                
            mid +=1


        