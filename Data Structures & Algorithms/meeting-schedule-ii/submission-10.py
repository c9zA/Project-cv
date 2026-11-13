"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        arr = []
        for interval in intervals:
            arr.append([interval.start, interval.end])
        ongoing = []
        ans = 0
        arr.sort()
        for s,e in arr:
            while ongoing and ongoing[0]<=s:
                heapq.heappop(ongoing)
            heapq.heappush(ongoing, e)
            ans = max(ans, len(ongoing))
        return ans