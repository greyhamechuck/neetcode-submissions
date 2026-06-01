class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length ==2:
            return max(nums[0],nums[1])
        elif length ==0:
            return 0
        
        def suprob(subnums: List[int]):
            prev1 = 0
            prev2= 0
            for i in subnums:
                current = max(prev2+i,prev1)
                prev2=prev1
                prev1=current

            return prev1

        scen1= suprob(nums[1:length])
        scen2= suprob(nums[0:length-1])

        return max(scen1,scen2)      
        