class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        lstart = intervals[0][0]
        lend = intervals[0][1]
        result = []
        result.append(intervals[0])
        for i in intervals[1:]:
            if i[0]>lend:
                result.append(i)
            elif i[0]<=lend:
                start = i[0]
                end = i[1]
                if start >= result[-1][0]:
                    result[-1][1] = max(end,result[-1][1])
                else:
                    result[-1][0] = start
                    result[-1][1] = max(end,result[-1][1])
            lstart = result[-1][0]
            lend = result[-1][1]
        return result