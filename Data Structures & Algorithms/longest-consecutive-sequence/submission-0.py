class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest =0
        for num in nums:
            if (num-1) not in numset:
                length =1
                while (num + length) in numset:
                    length +=1
                longest  = max(longest,length)
        return longest
        # mp = defaultdict(int)
        # res =0
        # for num in nums:
        #     if not mp[num]:
        #         mp[num] = mp[num-1] +mp[num+1] +1
        #         mp[num-mp[num-1]] = mp[num]
        #         mp[num+mp[num+1]] = mp[num]
        #         res  = max(res,mp[num])
        # return res