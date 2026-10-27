class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        path = []
        def back(start):
            temp = sorted(path)
            if temp not in res:
                res.append(temp)
            for i in range(start,n):
                path.append(nums[i])
                back(i+1)
                path.pop()

        back(0)
        return res