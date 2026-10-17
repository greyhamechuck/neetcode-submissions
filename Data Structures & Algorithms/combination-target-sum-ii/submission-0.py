class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def back(startindex,target_left,path):
            if target_left == 0:
                res.append(path.copy())
                return

            if target_left <0:
                return

            for i in range(startindex,len(candidates)):
                if i > startindex and candidates[i] == candidates[i - 1]:
                    continue

                number = candidates[i]
                path.append(number)
                back(i+1,target_left-number,path)
                path.pop()

        
        back(0,target,[])
        return res