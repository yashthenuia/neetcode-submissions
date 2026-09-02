class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax =[0]*n 
        leftmax[0]=height[0]
        
        rightmax=[0]*n
        rightmax[-1]= height[-1]
        for i in range(1,len(height)):
            leftmax[i]= max(leftmax[i-1],height[i])
            rightmax[n-i-1]= max(rightmax[n-i],height[n-i-1])
        ans =0
        for i in range (n):
            water = min(leftmax[i],rightmax[i]) - height[i]
            ans +=water
        return ans
        