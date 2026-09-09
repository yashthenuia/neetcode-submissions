class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ans = []
        for i in nums:
            dic[i] = dic.get(i,0)+1
        
        sortdic = sorted(dic.items(), key =lambda item: item[1],reverse =True)
        for i in range(k):
            ans.append(sortdic[i][0])
        return ans