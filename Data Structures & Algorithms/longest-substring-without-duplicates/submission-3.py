class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        compare = set()
        left = 0
        right = 0
        counter = 0
        current =0
        while right < len(s):
            if s[right] in compare:
                compare.remove(s[left])            
                left +=1
         
            else:
                current =right - left + 1
                counter = max(counter,current)
                compare.add(s[right])
                right +=1              
        return counter