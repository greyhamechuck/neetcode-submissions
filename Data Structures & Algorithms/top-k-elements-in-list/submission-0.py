class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1

        numbers = list(count.keys())
        sorted_list = sorted(numbers,key=count.get,reverse=True)

        return sorted_list[:k]