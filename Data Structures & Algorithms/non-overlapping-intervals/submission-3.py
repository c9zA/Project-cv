class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        removed = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                removed += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return removed