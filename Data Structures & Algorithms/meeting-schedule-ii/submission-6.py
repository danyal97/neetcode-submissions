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
        count = 0
        for i in range(len(intervals)):
            start,end = intervals[i].start, intervals[i].end
            if len(end_times) == 0:
                count+=1
                end_times.append(end)
            else:
                heapq.heappush(end_times,end)
                if start >= end_times[0]:
                    heapq.heappop(end_times) 
        print(end_times)
        return len(end_times)

        