"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n=len(intervals)
        starts = sorted(intervals[i].start for i in range(n))
        ends = sorted(intervals[i].end for i in range(n))
        if not intervals:
            return 0
        count = 0
        en = 0
        for start in starts:
            if start < ends[en]:
                count+=1
            else:
                en+=1

        return count