class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result =[]
        for interval in intervals:
                    # 如果结果集为空，或者当前区间的起点大于结果集最后一个区间的终点（无重叠）
                    if not result or interval[0] > result[-1][1]:
                        result.append(interval)
                    else:
                        # 有重叠，更新结果集最后一个区间的终点（取最大值）
                        result[-1][1] = max(result[-1][1], interval[1])
                        
        return result