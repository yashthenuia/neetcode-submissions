class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =[]
        heapq.heapify(heap)
        for i in stones:
            heapq.heappush(heap,-i)
        
        while len(heap)>1:
            i = -1* heapq.heappop(heap)
            j = -1 * heapq.heappop(heap)
            if i==j:
                continue
            else :
                heapq.heappush(heap,-1*abs(i-j))
        if len(heap)==0:
            return 0
        else :
            return -1*heap[0]

        