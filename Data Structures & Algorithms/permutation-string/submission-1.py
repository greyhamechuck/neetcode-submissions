from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        w1 = Counter(s1)
        w2 = Counter(s2[:len1])

        if w1 == w2:
            return True

        window1 = Counter(s1)
        window2= Counter(s2[:len1])
        for i in range(len1,len2):
            right = s2[i]
            left = s2[i - len1]
            window2[right] +=1
            window2[left] -=1
            if window2 == window1:
                return True
            
        return False
            