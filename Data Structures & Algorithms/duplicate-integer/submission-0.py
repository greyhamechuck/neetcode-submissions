class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        node = {}
        for i in nums:
            if i in node:
                return True
            else:
                node[i] = 1
        
        return False