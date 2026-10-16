from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        window1= Counter(s1)
        window2= Counter(s2[:len1])
        if window1 == window2:
            return True
        for i in range(len1,len2):
            right = s2[i]
            left = s2[i-len1]
            window2[left]-=1
            window2[right]+=1
            if window1==window2:
                return True
        return False            