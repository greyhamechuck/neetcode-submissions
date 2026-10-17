class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def back(startindex,path):
            res.append(path.copy())
            for i in range(startindex,n):
                path.append(nums[i])
                back(i+1,path)
                path.pop()

        back(0,[])
        return res