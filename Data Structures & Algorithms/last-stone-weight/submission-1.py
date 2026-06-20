class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)  # 原地堆化
        while len(heap)>1:
            un = heapq.heappop(heap)
            two = heapq.heappop(heap)
            if un==two:
                continue
            else:
                baby = abs(un-two)
                heapq.heappush(heap,-baby)
    
        if not heap:
            return 0
        else:
            return -heap[0]