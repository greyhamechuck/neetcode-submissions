
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nu = {}

        for i in nums:
            if i in nu:
                return True
            else:
                nu[i]=1
        
        return False