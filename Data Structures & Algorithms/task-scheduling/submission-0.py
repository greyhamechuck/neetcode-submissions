from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每个任务的数量
        counts = Counter(tasks)
        
        # 2. 找到出现次数最多的任务一共出现了多少次
        max_val = max(counts.values())
        
        # 3. 统计有多少个任务同样都达到了这个最高次数
        # 比如 A 有 3 个，B 也有 3 个，那么 max_count 就是 2
        max_count = sum(1 for cnt in counts.values() if cnt == max_val)
        
        # 4. 用公式直接计算出大框架所需要的最小时间
        # (max_val - 1) * (n + 1) 是前几组的总长度
        # + max_count 是最后一组尾巴上挂的任务数
        ans = (max_val - 1) * (n + 1) + max_count
        
        # 5. 如果任务极多把空位撑破了，直接返回 len(tasks)
        return max(ans, len(tasks))