class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        start = 0
        over = 0
        if sum(gas) < sum(cost):
            return -1
        for sp in range(length):
            over += gas[sp] - cost[sp] 
            if over < 0:
                start = sp+1
                over =0

        return start