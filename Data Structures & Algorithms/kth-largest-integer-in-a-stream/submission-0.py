class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        # 1. 将初始数组原地转化为堆结构
        heapq.heapify(self.heap)
        
        # 2. 如果初始数组的长度大于 k，就把多余的、比较小的元素全部弹出
        # 确保堆的规模维持在 k 
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 1. 新元素入堆
        heapq.heappush(self.heap, val)
        
        # 2. 如果堆的尺寸超过了 k，说明多了一个，弹出最小的那个（堆顶）
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. 此时的堆顶就是大小为 k 的堆中最小的元素，即第 k 大的元素
        return self.heap[0]