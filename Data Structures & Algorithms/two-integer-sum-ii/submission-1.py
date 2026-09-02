class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0 
        j = len(numbers) -1
        while i <j :
            ans = numbers[i] + numbers[j]
            if ans == target :
                return ([i+1,j+1])
            elif ans < target:
                i +=1
            else :
                j -=1
        

        