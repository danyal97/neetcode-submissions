"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals = sorted(intervals, key=lambda x: x.start)
        
        for i in range(0,len(intervals)-1):
            prev_start, prev_end =  intervals[i].start,intervals[i].end
            start, end =  intervals[i+1].start,intervals[i+1].end

            if start < prev_end:
                return False
            
        return True
