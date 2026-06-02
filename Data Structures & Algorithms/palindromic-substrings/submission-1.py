class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        result = 0
        def expander(left,right):
            counter = 0
            while left >=0 and right < length and s[right] == s[left]:
                left -=1
                right +=1
                counter +=1
            return counter

        for i in range(length):
            len1 = expander(i,i)
            len2 = expander(i,i+1)
            result += len1
            result += len2

        return result