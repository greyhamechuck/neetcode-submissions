"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True
        lstart = intervals[0].start
        lend = intervals[0].end
        for i in intervals[1:]:
            if i.start<lend:
                return False
            lstart = i.start
            lend = i.end
        return True
