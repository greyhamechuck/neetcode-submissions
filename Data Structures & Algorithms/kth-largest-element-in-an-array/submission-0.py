class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for i in nums:
            num = i
            heapq.heappush(result,num)
            if len(result)>k:
                heapq.heappop(result)

        for i in result:
            i = -i
        return result[0]