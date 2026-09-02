class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        le= len(nums)
        list1 = [nums[0]]
        list2 = [nums[-1]]
        res=[]
        for i in range (1,le):
            list1.append(list1[-1] * nums[i])
            list2.append(list2[-1]*nums[le-i-1])
        print(list1)
        print(list2)
        for i in range(le):
            if i==0:
                res.append(list2[le-i-2])
            elif i==(le-1):
                res.append(list1[le-2])
            else :
                res.append(list1[i-1]*list2[le-i-2])
        return res
        