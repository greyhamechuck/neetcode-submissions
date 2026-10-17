class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(startindex,target_left,path):
            if target_left == 0:
                res.append(path.copy())
                return

            if target_left < 0:
                return
            
            for i in range(startindex,n):
                number = nums[i]
                path.append(number)
                backtracking(i,target_left-number,path)
                path.pop()

        backtracking(0,target,[])

        return res