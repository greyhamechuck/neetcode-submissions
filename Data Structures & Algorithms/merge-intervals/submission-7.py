class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        n = len(intervals)
        intervals.sort()
        leftend=intervals[0][0]
        rightend=intervals[0][1]
        res = [intervals[0]]
        for i in range(1,n):
            if rightend>=intervals[i][0]>=leftend:
                if intervals[i][1]> rightend:
                    res[-1][1] =  intervals[i][1]
                    rightend = res[-1][1]

            else:
                res.append(intervals[i])
                leftend = intervals[i][0]
                rightend = intervals[i][1]
            
        return res