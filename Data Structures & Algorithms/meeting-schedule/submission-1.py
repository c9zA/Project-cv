"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = []
        for inst in intervals:
            arr.append([inst.start, inst.end])
        arr.sort()
        lastEnd = -1
        for s,e in arr:
            if lastEnd>s:
                return False
            lastEnd = e
        return True