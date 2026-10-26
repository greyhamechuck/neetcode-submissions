class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(start,stack):
            res.append(stack.copy())
            for st in range(start,n):
                stack.append(nums[st])
                backtracking(st+1,stack)
                stack.pop()

        backtracking(0,[])
        return res
        