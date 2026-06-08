class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        compare = {}  # 真正的账本：记录当前窗口里每个字符出现的次数
        left1 = 0     # 左边界
        left2 = 0     # 右边界
        max_freq = 0  # 窗口内任何字符出现过的最高频率（多数党选票）
        result = 0
        
        while left2 < len(s):
            # 1. 右边界字符进窗，登记入账
            compare[s[left2]] = compare.get(s[left2], 0) + 1
            # 动态更新全场最高频次
            max_freq = max(max_freq, compare[s[left2]])
            
            # 2. 核心物理公式：当前窗口总长度 (left2 - left1 + 1) - 多数党选票
            # 如果杂质数量大于额度 k，说明撑破了！
            # 🚨 对应你的 else -> else（额度用光），这里用 if 拦截，让左墙前进一步
            if (left2 - left1 + 1) - max_freq > k:
                compare[s[left1]] -= 1  # 真正的额度收回：吐出谁，谁的频次就减 1
                left1 += 1              # 左墙壁前进一步
            
            # 3. 只要没被上面的 if 拦截，说明当前窗口绝对合法，高高兴兴量身高
            result = max(result, left2 - left1 + 1)
            
            # 4. 快指针无脑右移，开拓疆土
            left2 += 1
            
        return result