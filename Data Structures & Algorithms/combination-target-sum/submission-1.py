class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        def back(start,target_left,path):
            if target_left ==0:
                result.append(path.copy())
                return 
            if target_left < 0:
                return
            for st in range(start,n):
                path.append(nums[st])
                back(st,target_left-nums[st],path)
                path.pop()

        back(0,target,[])
        return result