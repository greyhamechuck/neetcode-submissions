class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        muse={}
        final = []
        for i in nums:
            if i not in muse:
                muse[i] = 1
            else:
                muse[i] +=1
        

        for i in muse:
            if muse[i] == 1:
                final.append(i)


        return final[0]