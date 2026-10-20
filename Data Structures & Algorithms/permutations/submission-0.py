class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        path = []
        def backtracking():
            if len(path) == n:
                res.append(path.copy())
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtracking()
                    path.pop()

        
        backtracking()
        return res

            
