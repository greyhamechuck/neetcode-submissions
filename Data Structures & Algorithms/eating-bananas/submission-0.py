import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. 定义答案的可能范围（闭区间）
        left = 1
        right = max(piles)
        
        # 记录最终抓到的最小速度
        ans = right 
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # 计算以 mid 的速度吃完所有香蕉需要多少小时
            total_hours = 0
            for pile in piles:
                # math.ceil 是向上取整，比如 3 根香蕉速度 2，需要 2 小时
                total_hours += math.ceil(pile / mid)
                
            # 2. 判定逻辑
            if total_hours <= h:
                # 说明 mid 速度够快，能在 h 小时内吃完。
                # 这是一个潜在答案，先记下来
                ans = mid
                # 既然能吃完，我们尝试更慢一点的速度，看看行不行
                right = mid - 1
            else:
                # 说明 mid 速度太慢了，规定时间内吃不完。
                # 必须调大速度
                left = mid + 1
                
        return ans