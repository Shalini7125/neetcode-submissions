import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap1=[-x for x in stones]
        heapq.heapify(heap1)
        while(len(heap1)>1):
            x=-heapq.heappop(heap1)
            y=-heapq.heappop(heap1)
            if(abs(-x+y)):
                heapq.heappush(heap1,-abs(-x+y))
        return -heap1[0] if heap1 else 0

        