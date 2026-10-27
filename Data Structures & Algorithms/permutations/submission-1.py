class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def back():
            if len(path) == n:
                res.append(path.copy())

            for num in nums:
                if num not in path:
                    path.append(num)
                    back()
                    path.pop()

        back()
        return res