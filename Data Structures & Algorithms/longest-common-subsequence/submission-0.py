class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        if l1 == l2:
            if text1 == text2:
                return l1
        
        if not text1 or not text2:
            return 0
        

        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

                # 核心修正 2：从 1 开始遍历，完美避开索引 -1 的尴尬
        for i in range(1, l1 + 1):
                    for j in range(1, l2 + 1):
                        # 因为 dp 挪了一位，对应的字符串字符要看 i-1 和 j-1
                        if text1[i - 1] == text2[j - 1]:
                            # 撞衫了：等于左上角（残局）的结果 + 1
                            dp[i][j] = dp[i - 1][j - 1] + 1
                        else:
                            # 没撞衫：从【上面传下来的】和【左边传过来的】里面挑一个最大的继承
                            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                # 右下角就是最终完美账本的终点
        return dp[l1][l2]