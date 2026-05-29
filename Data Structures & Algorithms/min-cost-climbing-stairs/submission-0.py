class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p =q =0
        n = len(cost)
        for i in range(2,n+1):
            counter = min(p+cost[i-2],q+cost[i-1])
            p=q
            q=counter

        return q