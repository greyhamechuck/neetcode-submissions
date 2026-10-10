from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        table = Counter(hand)
        sorted_keys = sorted(table.keys())
        if len(hand) % groupSize != 0:
            return False 
        for num in sorted_keys:
            freq = table[num]
            if freq > 0:
                for i in range(groupSize):
                    table[i+num] -= freq
                    if table[i+num] < 0:
                        return False
                    
                    
        return True