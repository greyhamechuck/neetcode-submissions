class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x: x[1])
        lstart = intervals[0][0]
        lend = intervals[0][1]
        counter =0 
        for i in intervals[1:]:
            if i[0]<lend:
                counter+=1
            else:
                lend = i[1]
        return counter