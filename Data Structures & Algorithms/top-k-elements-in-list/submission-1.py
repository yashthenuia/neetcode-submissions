class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        ans =[]
        for i in nums:
            dicts[i]  = dicts.get(i,0) +1
        
        # Sort dictionary items by value (frequency) in descending order
        sorted_items = sorted(dicts.items(), key=lambda item: item[1], reverse=True)
       
        # Take the keys of the first k items
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans