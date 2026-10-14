class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dick = {}
        left = 0
        result =0
        for right,ch in enumerate(s):
            if ch in dick:
                left = max(left,dick[ch]+1)
            dick[ch] = right
            result = max(result,right-left+1)
        
        return result

