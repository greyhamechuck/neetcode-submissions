class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
          if dp[i] == True:

            for j in range(i+1,len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
                        
        return dp[len(s)]