class Solution:
    def climbStairs(self, n: int) -> int:

        if n <2:
            return 1
        p = 1
        q =2
        counter = 0
        for i in range(3,n+1):
            counter = p+q
            p = q
            q = counter
        
        return q