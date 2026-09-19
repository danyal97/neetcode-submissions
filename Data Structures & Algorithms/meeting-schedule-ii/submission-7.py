"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals = sorted(intervals, key = lambda x: x.start)
        end_times = []
        
        for i in range(len(intervals)):
            start,end = intervals[i].start, intervals[i].end
            if len(end_times) == 0:
                heapq.heappush(end_times,end)
            else:            
                if start >= end_times[0]:
                    heapq.heappop(end_times)
                    heapq.heappush(end_times,end)
                else:
                    heapq.heappush(end_times,end)

        return len(end_times)

        