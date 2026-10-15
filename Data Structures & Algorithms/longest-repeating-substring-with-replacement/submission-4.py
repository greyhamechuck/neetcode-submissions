class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dick = {}
        left = 0
        credit = k
        result = 0
        max_freq = 0  
        
        for right, ch in enumerate(s):
            dick[ch] = dick.get(ch, 0) + 1
            
            max_freq = max(max_freq, dick[ch])

            if (right - left + 1) - max_freq > k:
                dick[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result