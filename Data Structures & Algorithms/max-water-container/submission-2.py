class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start,end = 0, len(heights)-1
        ans =0
        while start< end:
            water = (end-start)*(min(heights[start],heights[end]))
            # print(f"{ans},,,,{start},,,,{end}")
            ans = max(ans,water)
            if heights[start] < heights[end]:
                start +=1
            else:
                 end  -=1
        return ans 