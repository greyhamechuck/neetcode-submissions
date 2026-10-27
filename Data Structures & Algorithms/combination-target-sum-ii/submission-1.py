class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def back(start,target_left,path):
            if target_left == 0:
                res.append(path.copy())

            elif target_left<0:
                return

            for i in range(start,n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                back(i+1,target_left-candidates[i], path)
                path.pop()

        back(0,target,[])

        return res
