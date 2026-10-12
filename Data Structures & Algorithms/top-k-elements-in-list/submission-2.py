class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.keys(),key = count.get,reverse = True)
        result = []
        for i in range(k):
            result.append(count[i])
        
        return result